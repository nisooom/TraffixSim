
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


class RoadType(Enum):
    NONE                   = auto()
    STRAIGHT               = auto()
    TURN                   = auto()
    THREE_WAY_INTERSECTION = auto()
    FOUR_WAY_INTERSECTION  = auto()


# map to get the rotations of each road for each case
rotations_dict = {
    RoadType.STRAIGHT: {
        "north-south": 0,
        "east-west": 180,
    },
    RoadType.TURN: {
        "north-east": 90,
        "north-west": 0,
        "south-east": 180,
        "south-west": 270,
    },
    RoadType.THREE_WAY_INTERSECTION: {
        "west-north-east": 0,
        "north-east-south": 90,
        "east-south-west": 180,
        "south-west-north": 270,
    }
}


def _get_region(x: int, y: int) -> image.TextureRegion:
    region: image.TextureRegion = road_sprite_sheet.get_region(x*64, y*64, 64, 64)
    region.anchor_x = 32
    region.anchor_y = 32
    return region


def _get_straight_road(type: str) -> sprite.Sprite:
    tex = _get_region(2, 2)
    out = sprite.Sprite(tex)
    out.rotation = rotations_dict[RoadType.STRAIGHT][type]
    return out


def _get_turn_road(type: str) -> sprite.Sprite:
    tex = _get_region(2, 1)
    out = sprite.Sprite(tex)
    out.rotation = rotations_dict[RoadType.TURN][type]
    return out


def _get_three_way_intersection_road(type: str) -> sprite.Sprite:
    tex = _get_region(4, 1)
    out = sprite.Sprite(tex)
    out.rotation = rotations_dict[RoadType.THREE_WAY_INTERSECTION][type]
    return out


def _get_four_way_intersection_road(_: str) -> sprite.Sprite:
    tex = _get_region(0, 0)
    out = sprite.Sprite(tex)
    return out


def _get_none_road(_: str) -> sprite.Sprite:
    out = sprite.Sprite(none_road_tex)
    return out


def get_sprite(type: RoadType, info: str) -> sprite.Sprite:
    road_sprite_map = {
        RoadType.NONE: _get_none_road,
        RoadType.STRAIGHT: _get_straight_road,
        RoadType.TURN: _get_turn_road,
        RoadType.THREE_WAY_INTERSECTION: _get_three_way_intersection_road,
        RoadType.FOUR_WAY_INTERSECTION: _get_four_way_intersection_road,
    }
    return road_sprite_map[type](info)


class RoadTile:

    def __init__(self, position: tuple[int, int], type: RoadType, info: str = ""):
        self.position = position
        self.type = type
        self.info = info

        self.sprite: sprite.Sprite = get_sprite(type, info)

        self.sprite.position = (
            position[1] * simulation_map_attrs["tile_size"],
            position[0] * simulation_map_attrs["tile_size"],
            0
        )
        self.sprite.scale = simulation_map_attrs["tile_size"] / 64
