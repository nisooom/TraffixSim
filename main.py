
from src.user_inputs import handle_user_input
from src.common import display_window
import pyglet
from src.tileset import TileSet

# TODO: add clamps on grids so that we can add gui on the side.

label = pyglet.text.Label(
    "TraffixSim",
    font_name="Consolas", font_size=40,
    x=display_window.width / 2, y=display_window.height / 2 + 10,
    anchor_x='center', anchor_y='center'
)

names = pyglet.text.Label("By Siddharth, Nishumbh, Dev, Hamza.", font_name="Consolas", font_size=17,
                          x=display_window.width / 2, y=display_window.height / 2 - 28,
                          anchor_x='center', anchor_y='center')

tiles = TileSet()


@display_window.event
def on_draw():
    display_window.clear()
    tiles.draw()

    # label.draw()
    # names.draw()


pyglet.clock.schedule_interval(handle_user_input, 1/30)
pyglet.clock.schedule_interval(tiles.handle_mouse_click, 1/30)
pyglet.app.run()
