
from src.common import mouse_handler, camera_attrs
import pyglet
from enum import Enum, auto


class TileSet:

    class TileType(Enum):
        TURN = auto()
        STRAIGHT = auto()
        STRAIGHT_TURN = auto()
        ROAD_END = auto()
        INTERSECTION = auto()
        NON_ROAD = auto()
        START = auto()
        END = auto()

    colors = {
        TileType.TURN: (255, 0, 0),  # Red
        TileType.STRAIGHT: (0, 0, 255),  # Blue
        TileType.STRAIGHT_TURN: (0, 255, 0),  # Green
        TileType.ROAD_END: (255, 255, 0),  # Yellow
        TileType.INTERSECTION: (255, 165, 0),  # Orange
        TileType.NON_ROAD: (128, 128, 128)  # Gray
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
                tile_type = self.TileType.NON_ROAD  # Default type
                tile = Tile(col, row, tile_type)
                rectangle = pyglet.shapes.BorderedRectangle(
                    x=col*self.tile_size, y=row*self.tile_size,
                    width=self.tile_size, height=self.tile_size,
                    color=self.get_color(tile_type), batch=self.batch
                )
                tile.rect = rectangle  # Storing the rectangle in the Tile instance
                self.tiles[row][col] = tile

    def draw(self):
        self.batch.draw()

    def get_color(self, type: TileType):
        return self.colors[type]

    def handle_mouse_click(self, dt: float):
        if not mouse_handler[pyglet.window.mouse.LEFT]:
            return
        
        x = mouse_handler['x'] - int(camera_attrs['position'][0])
        y = mouse_handler['y'] - int(camera_attrs['position'][1])

        adjusted_tile_size = self.tile_size * camera_attrs['scale']
        tile_col = int(x / adjusted_tile_size)
        tile_row = int(y / adjusted_tile_size)

        if tile_col not in range(self.columns) or tile_row not in range(self.rows):
            return

        clicked_tile = self.tiles[tile_row][tile_col]
        clicked_tile.tile_type = self.TileType.INTERSECTION
        clicked_tile.rect.color = self.get_color(clicked_tile.tile_type)


class Tile:
    def __init__(self, x: int, y: int, tile_type: TileSet.TileType):
        self.tile_type = tile_type
        self.x = x
        self.y = y
        self.rect: pyglet.shapes.Rectangle = None
