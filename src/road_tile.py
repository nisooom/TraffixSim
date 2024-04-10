
from src.common import simulation_map_attrs
from pyglet import sprite, image
from pyglet.gl import *
from enum import Enum, auto


road_sprite_sheet_img: image.ImageData = image.load('assets/new_roads/roads2W.png')
road_sprite_sheet: image.Texture = road_sprite_sheet_img.get_texture()
# making the texture crisp (no blurring)
# glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
# glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

none_road_img: image.ImageData = image.create(64, 64, image.SolidColorImagePattern((160, 192, 112, 255)))
none_road_tex: image.Texture = none_road_img.get_texture()
none_road_tex.anchor_x = 32
none_road_tex.anchor_y = 32


class Direction(Enum):
    NORTH = auto()
    EAST  = auto()
    WEST  = auto()
    SOUTH = auto()


def _get_region(x: int, y: int) -> image.TextureRegion:
    region: image.TextureRegion = road_sprite_sheet.get_region(x*64, y*64, 64, 64)
    region.anchor_x = 32
    region.anchor_y = 32
    return region


# map to get the rotations of each road for each case
texregion_rotation_dict: dict[tuple[Direction, ...], tuple[image.TextureRegion, int]] = {
    (): (none_road_tex, 0), # none road
    (Direction.NORTH, Direction.SOUTH): (_get_region(2, 2), 1), # straight road
    (Direction.EAST,  Direction.WEST ): (_get_region(2, 2), 0), # straight road
    (Direction.NORTH, Direction.EAST ): (_get_region(2, 1), 1), # turn road
    (Direction.NORTH, Direction.WEST ): (_get_region(2, 1), 0), # turn road
    (Direction.EAST,  Direction.SOUTH): (_get_region(2, 1), 2), # turn road
    (Direction.WEST,  Direction.SOUTH): (_get_region(2, 1), 3), # turn road
    (Direction.NORTH, Direction.EAST,  Direction.WEST ): (_get_region(4, 1), 0), # three way intersection
    (Direction.NORTH, Direction.EAST,  Direction.SOUTH): (_get_region(4, 1), 1), # three way intersection
    (Direction.EAST,  Direction.WEST,  Direction.SOUTH): (_get_region(4, 1), 2), # three way intersection
    (Direction.NORTH, Direction.WEST,  Direction.SOUTH): (_get_region(4, 1), 3), # three way intersection
    (Direction.NORTH, Direction.EAST, Direction.WEST, Direction.SOUTH): (_get_region(0, 0), 0) # four way intersection
}


def get_sprite(d_tup: tuple[Direction, ...]) -> sprite.Sprite:
    region, rot = texregion_rotation_dict[d_tup]
    out = sprite.Sprite(region)
    out.rotation = rot * 90
    return out


class RoadTile:

    def __init__(self, position: tuple[int, int], d_tup: tuple[Direction, ...]):
        self.position = position
        self.d_tup = d_tup

        self.sprite: sprite.Sprite = get_sprite(d_tup)

        self.sprite.position = (
            position[1] * simulation_map_attrs["tile_size"],
            position[0] * -simulation_map_attrs["tile_size"],
            0
        )
        self.sprite.scale = simulation_map_attrs["tile_size"] / 64

    def __repr__(self) -> str:
        return f"RoadTile({self.position=}, {self.type=}, {self.info=}, {self.sprite.position=})"
