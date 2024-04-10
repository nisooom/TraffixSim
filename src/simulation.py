
import random
from src.common import mouse_handler, camera_attrs, simulation_map_attrs
from src.road_tile import Direction, RoadTile
import pyglet
random.seed(0)


class Simulation:

    def __init__(self):
        self.road_tiles: list[list[RoadTile]] = [
            [None for _ in range(simulation_map_attrs["num_cols"])]
            for _ in range(simulation_map_attrs["num_rows"])
        ]
        self.batch = pyglet.graphics.Batch()
        self.road_group = pyglet.graphics.Group(order=0)
        self.vehicle_group = pyglet.graphics.Group(order=1)

        _dummy_data = [
            (),
            (Direction.NORTH, Direction.SOUTH),
            (Direction.EAST,  Direction.WEST ),
            (Direction.NORTH, Direction.EAST ),
            (Direction.NORTH, Direction.WEST ),
            (Direction.EAST,  Direction.SOUTH),
            (Direction.WEST,  Direction.SOUTH),
            (Direction.NORTH, Direction.EAST,  Direction.WEST ),
            (Direction.NORTH, Direction.EAST,  Direction.SOUTH),
            (Direction.EAST,  Direction.WEST,  Direction.SOUTH),
            (Direction.NORTH, Direction.WEST,  Direction.SOUTH),
            (Direction.NORTH, Direction.EAST, Direction.WEST, Direction.SOUTH),
        ]

        for r in range(simulation_map_attrs["num_rows"]):
            for c in range(simulation_map_attrs["num_cols"]):
                d_tup = random.choice(_dummy_data)
                self.road_tiles[r][c] = RoadTile((r, c), d_tup)
                self.road_tiles[r][c].sprite.group = self.road_group
                self.road_tiles[r][c].sprite.batch = self.batch

    def draw(self):
        self.batch.draw()
