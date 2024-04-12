
import pyglet
from pyglet.window import Window, key, mouse


window_width = 800
window_height = 800


display_window = Window(
    width=window_width, height=window_height,
    caption="TraffixSim"
)

_window_icon = pyglet.image.load("assets/window_icon/window_icon(32x32).png")
display_window.set_icon(_window_icon)


key_handler = key.KeyStateHandler()
mouse_handler = mouse.MouseStateHandler()

display_window.push_handlers(key_handler, mouse_handler)


simulation_map_attrs = {
    'num_rows': 5,
    'num_cols': 5,
    'tile_size': 64,
}


camera_attrs = {
    'position': [0.0, 0.0, 0.0],
    'scale': 1.0,
}
