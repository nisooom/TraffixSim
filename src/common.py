
import pyglet
from pyglet.window import Window, key, mouse


display_window = Window(
    width=800, height=800,
    caption="TraffixSim"
)

_window_icon = pyglet.image.load("assets/window_icon/window_icon(32x32).png")
display_window.set_icon(_window_icon)


key_handler = key.KeyStateHandler()
mouse_handler = mouse.MouseStateHandler()

display_window.push_handlers(key_handler, mouse_handler)
