
import random
import pyglet


vehicle_sprite_sheet = pyglet.image.load('assets/vehicles/sprite_sheet.png').get_texture()
# the region we are interested in is from (62, 0) to (422, 336)
# the region contains 3 rows and 6 columns of vehicles

# (422 - 62) / 6
vehicle_width = 60
# (336 - 0) / 3 = 112
vehicle_height = 112


def get_random_vehicle_image() -> pyglet.image.ImageDataRegion:
    x = random.randrange(6)
    y = random.randrange(3)

    region_x = 62 + x * vehicle_width
    # since opengl's y coord is at bottom we subtract from image_height
    region_y = 560 - (y+1) * vehicle_height

    region = vehicle_sprite_sheet.get_region(region_x, region_y, vehicle_width, vehicle_height)
    region.anchor_x = region.width // 2
    region.anchor_y = region.height // 2
    return region


class Vehicle(pyglet.sprite.Sprite):

    main_batch = pyglet.graphics.Batch()

    def __init__(self):
        image = get_random_vehicle_image()
        super().__init__(image, batch=Vehicle.main_batch)

    @staticmethod
    def draw_all():
        Vehicle.main_batch.draw()
