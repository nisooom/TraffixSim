
from src.common import display_window
import pyglet


label = pyglet.text.Label(
    "TraffixSim",
    font_name="Consolas", font_size=40,
    x=display_window.width/2, y=display_window.height/2,
    anchor_x='center', anchor_y='center'
)


@display_window.event
def on_draw():
    display_window.clear()

    label.draw()


pyglet.app.run()
