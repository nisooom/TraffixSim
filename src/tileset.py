
from src.common import mouse_handler, camera_attrs
import pyglet
from enum import Enum, auto


road_sprite_sheet = pyglet.image.load('assets/new_roads/roads2W.png').get_texture()


def _get_region(x: int, y: int) -> pyglet.image.TextureRegion:
    region = road_sprite_sheet.get_region(x*64, 192-y*64, 64, 64)
    region.anchor_x = 32
    region.anchor_y = 32
    return region


def get_road_image(type: 'TileType') -> pyglet.image.TextureRegion:
    match type:
        case TileType.TURN:
            return _get_region(2, 1)
        case TileType.STRAIGHT:
            return _get_region(2, 0)
        case TileType.STRAIGHT_TURN:
            return _get_region(3, 1)
        case TileType.ROAD_END:
            return _get_region(4, 0)
        case TileType.INTERSECTION:
            return _get_region(0, 2)
        case TileType.NON_ROAD:
            return _get_region(1, 2)
        case TileType.START:
            return _get_region(0, 0)
        case TileType.END:
            return _get_region(0, 0)
        case _:
            raise Exception('No such type')


class TileType(Enum):
    TURN = auto()
    STRAIGHT = auto()
    STRAIGHT_TURN = auto()
    ROAD_END = auto()
    INTERSECTION = auto()
    NON_ROAD = auto()
    START = auto()
    END = auto()


class TileSet:

    type_img_map = {
        TileType.TURN: get_road_image(TileType.TURN),
        TileType.STRAIGHT: get_road_image(TileType.STRAIGHT),
        TileType.STRAIGHT_TURN: get_road_image(TileType.STRAIGHT_TURN),
        TileType.ROAD_END: get_road_image(TileType.ROAD_END),
        TileType.INTERSECTION: get_road_image(TileType.INTERSECTION),
        TileType.NON_ROAD: get_road_image(TileType.NON_ROAD),
        TileType.START: get_road_image(TileType.START),
        TileType.END: get_road_image(TileType.END),
    }

    def __init__(self, rows: int = 30, columns: int = 30, size: int = 16):
        self.rows = rows
        self.columns = columns
        self.tile_size = size
        self.batch = pyglet.graphics.Batch()

        self.tiles: list[list[Tile]] = [
            [None for _ in range(self.columns)]
            for _ in range(self.rows)
        ]

        self.init_tiles()

    def init_tiles(self):
        for row in range(self.rows):
            for col in range(self.columns):
                tile_type = TileType.NON_ROAD  # Default type
                tile = Tile(col, row, tile_type)

                tile.sprite = pyglet.sprite.Sprite(TileSet.type_img_map[tile_type], batch=self.batch)
                tile.sprite.scale = self.tile_size / 64
                tile.sprite.position = (
                    col*self.tile_size,
                    row*self.tile_size,
                    0
                )

                self.tiles[row][col] = tile

    def draw(self):
        self.batch.draw()

    def get_color(self, type: TileType):
        return self.colors[type]

    def handle_mouse_click(self, dt: float):
        if not mouse_handler[pyglet.window.mouse.LEFT]:
            return
        
        x = mouse_handler['x'] - int(camera_attrs['position'][0]) + self.tile_size//2
        y = mouse_handler['y'] - int(camera_attrs['position'][1]) + self.tile_size//2

        adjusted_tile_size = self.tile_size * camera_attrs['scale']
        tile_col = int(x / adjusted_tile_size)
        tile_row = int(y / adjusted_tile_size)

        if tile_col not in range(self.columns) or tile_row not in range(self.rows):
            return

        clicked_tile = self.tiles[tile_row][tile_col]
        clicked_tile.tile_type = TileType.INTERSECTION
        clicked_tile.sprite.image = TileSet.type_img_map[clicked_tile.tile_type]


class Tile:
    def __init__(self, x: int, y: int, tile_type: TileType):
        self.tile_type = tile_type
        self.x = x
        self.y = y
        self.sprite: pyglet.sprite.Sprite = None
