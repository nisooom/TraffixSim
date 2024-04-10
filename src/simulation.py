
import random
from src.common import mouse_handler, camera_attrs, simulation_map_attrs
from src.road_tile import RoadType, RoadTile
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

        _dummy_data = []
        _dummy_data.append((RoadType.NONE, ""))
        _dummy_data.extend((RoadType.STRAIGHT, info) for info in ("north-south", "east-west"))
        _dummy_data.extend((RoadType.TURN, info) for info in ("north-east", "north-west", "south-east", "south-west"))
        _dummy_data.extend((RoadType.THREE_WAY_INTERSECTION, info) for info in ("west-north-east", "north-east-south", "east-south-west", "south-west-north"))
        _dummy_data.append((RoadType.FOUR_WAY_INTERSECTION, ""))

        for i in range(simulation_map_attrs["num_cols"]):
            for j in range(simulation_map_attrs["num_rows"]):
                type, info = random.choice(_dummy_data)
                self.road_tiles[i][j] = RoadTile((i, j), type, info)
                self.road_tiles[i][j].sprite.group = self.road_group
                self.road_tiles[i][j].sprite.batch = self.batch

    def draw(self):
        self.batch.draw()