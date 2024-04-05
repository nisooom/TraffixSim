
from src.user_inputs import handle_user_input
from src.common import display_window
from src.vehicle import Vehicle
from src.tileset import TileSet
import pyglet

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

vehicles = []
for y in range(15):
    for x in range(15):
        v = Vehicle()
        v.scale = 0.2
        v.position = ((x+1)*30, (y+1)*30, 0)
        vehicles.append(v)


@display_window.event
def on_draw():
    display_window.clear()
    tiles.draw()

    Vehicle.draw_all()
    # label.draw()
    # names.draw()


pyglet.clock.schedule_interval(handle_user_input, 1/30)
pyglet.clock.schedule_interval(tiles.handle_mouse_click, 1/30)
pyglet.app.run()
