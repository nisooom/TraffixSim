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
tiles.createTiles()


@display_window.event
def on_draw():
    display_window.clear()
    tiles.drawTiles()

    # label.draw()
    # names.draw()


@display_window.event
def on_mouse_press(x, y, button, modifiers):
    tiles.on_mouse_press(x, y, button, modifiers)


pyglet.app.run()
