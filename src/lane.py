
from src.direction import Direction
import pyglet


class Lane:

    batch = pyglet.graphics.Batch()

    def __init__(self, road: 'RoadTile', start_d: Direction, stop_d: Direction):
        self.road = road
        self.start_d = start_d
        self.stop_d = stop_d

        self.vehicle_positions = self._get_vehicle_positions()

        self.circles = [
            pyglet.shapes.Circle(pos[0], pos[1], 1.0, batch=Lane.batch)
            for pos in self.vehicle_positions
        ]

    def _get_vehicle_positions(self) -> list[tuple[int, int]]:
        sp = self.road.sprite.position
        match (self.road.d_tup, self.start_d, self.stop_d):
            case ((Direction.NORTH, Direction.SOUTH), Direction.NORTH, Direction.SOUTH):
                return [
                    (sp[0]-5, sp[1]-24),
                    (sp[0]-5, sp[1]-12),
                    (sp[0]-5, sp[1]   ),
                    (sp[0]-5, sp[1]+12),
                    (sp[0]-5, sp[1]+24),
                ]
            case ((Direction.NORTH, Direction.SOUTH), Direction.SOUTH, Direction.NORTH):
                return [
                    (sp[0]+5, sp[1]-24),
                    (sp[0]+5, sp[1]-12),
                    (sp[0]+5, sp[1]   ),
                    (sp[0]+5, sp[1]+12),
                    (sp[0]+5, sp[1]+24),
                ]
            case ((Direction.EAST, Direction.WEST), Direction.EAST, Direction.WEST):
                return [
                    (sp[0]-24, sp[1]-5),
                    (sp[0]-12, sp[1]-5),
                    (sp[0]   , sp[1]-5),
                    (sp[0]+12, sp[1]-5),
                    (sp[0]+24, sp[1]-5),
                ]
            case ((Direction.EAST, Direction.WEST), Direction.WEST, Direction.EAST):
                return [
                    (sp[0]-24, sp[1]+5),
                    (sp[0]-12, sp[1]+5),
                    (sp[0]   , sp[1]+5),
                    (sp[0]+12, sp[1]+5),
                    (sp[0]+24, sp[1]+5),
                ]
            case ((Direction.NORTH, Direction.WEST), Direction.NORTH, Direction.WEST):
                return [
                    (sp[0]+5,  sp[1]+24),
                    (sp[0]+5,  sp[1]+12),
                    (sp[0]+2,  sp[1]-2 ),
                    (sp[0]-12, sp[1]-5 ),
                    (sp[0]-24, sp[1]-5 ),
                ]
            case ((Direction.NORTH, Direction.WEST), Direction.WEST, Direction.NORTH):
                return [
                    (sp[0]-5,  sp[1]+24),
                    (sp[0]-5,  sp[1]+12),
                    (sp[0]-7,  sp[1]+7 ),
                    (sp[0]-12, sp[1]+5 ),
                    (sp[0]-24, sp[1]+5 ),
                ]
            case ((Direction.NORTH, Direction.EAST), Direction.NORTH, Direction.EAST):
                return [
                    (sp[0]+5,  sp[1]+24),
                    (sp[0]+5,  sp[1]+12),
                    (sp[0]+7,  sp[1]+7 ),
                    (sp[0]+12, sp[1]+5 ),
                    (sp[0]+24, sp[1]+5 ),
                ]
            case ((Direction.NORTH, Direction.EAST), Direction.EAST, Direction.NORTH):
                return [
                    (sp[0]-5,  sp[1]+24),
                    (sp[0]-5,  sp[1]+12),
                    (sp[0]-2,  sp[1]-2 ),
                    (sp[0]+12, sp[1]-5 ),
                    (sp[0]+24, sp[1]-5 ),
                ]
            case ((Direction.EAST, Direction.SOUTH), Direction.EAST, Direction.SOUTH):
                return [
                    (sp[0]+24, sp[1]+5),
                    (sp[0]+12, sp[1]+5),
                    (sp[0]-2,  sp[1]+2),
                    (sp[0]-5,  sp[1]-12),
                    (sp[0]-5,  sp[1]-24),
                ]
            case ((Direction.EAST, Direction.SOUTH), Direction.SOUTH, Direction.EAST):
                return [
                    (sp[0]+5, sp[1]+5),
                    (sp[0]+5, sp[1]+5),
                    (sp[0]-2,  sp[1]+2),
                    (sp[0]+12,  sp[1]-12),
                    (sp[0]+24,  sp[1]-24),
                ]
        return []
