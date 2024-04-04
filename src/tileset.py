from src.common import display_window
import pyglet
from enum import Enum, auto


class TileSet():

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

    def __init__(self, rows=50, columns=50):
        self.width = display_window.width
        self.height = display_window.height
        self.rows = rows
        self.columns = columns
        self.tileSize = (self.width // columns, self.height // rows)
        self.batch = pyglet.graphics.Batch()

        self.tiles = [[]]

    def createTiles(self):
        self.tiles = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        for y in range(self.rows):
            for x in range(self.columns):
                tile_type = self.TileType.NON_ROAD  # Default type
                tile = Tile(x * self.tileSize[0], y * self.tileSize[1], tile_type)
                rectangle = pyglet.shapes.Rectangle(x * self.tileSize[0], y * self.tileSize[1],
                                                    self.tileSize[0] - 1, self.tileSize[1] - 1,
                                                    self.colors.get(tile_type), batch=self.batch)
                tile.rectangle = rectangle  # Storing the rectangle in the Tile instance
                self.tiles[y][x] = tile

    def drawTiles(self):
        self.batch.draw()

    def getColor(self, type):
        return self.colors.get(type)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            grid_x = x // self.tileSize[0]
            grid_y = y // self.tileSize[1]

            clicked_tile = self.tiles[grid_y][grid_x]

            clicked_tile.tileType = self.TileType.INTERSECTION
            clicked_tile.rectangle.color = self.colors.get(self.TileType.INTERSECTION)


class Tile:
    def __init__(self, x, y, tile_type):
        self.tileType = tile_type
        self.x = x
        self.y = y
        self.rect= None
