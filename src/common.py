
import pyglet


display_window = pyglet.window.Window(
    width=800, height=450,
    caption="TraffixSim"
)

clock = pyglet.clock.get_default()


_window_icon = pyglet.image.load("assets/window_icon/window_icon(32x32).png")
display_window.set_icon(_window_icon)
