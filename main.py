
from src.user_inputs import handle_user_input
from src.common import display_window
from src.simulation import Simulation
import pyglet

# TODO: add clamps on grids so that we can add gui on the side.

simulation = Simulation()


@display_window.event
def on_draw():
    display_window.clear()
    simulation.draw()


pyglet.clock.schedule_interval(handle_user_input, 1/30)
# pyglet.clock.schedule_interval(tiles.handle_mouse_click, 1/30)
pyglet.app.run()
