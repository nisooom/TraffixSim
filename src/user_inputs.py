
from src.common import display_window, key_handler
import pyglet


camera_position = [0, 0, 0]
camera_zoom = 1


def _update_view_matrix():
    view_mat = pyglet.math.Mat4()
    view_mat = view_mat.translate(camera_position)
    view_mat = view_mat.scale([camera_zoom, camera_zoom, 1])
    display_window.view = view_mat


def handle_camera_movement(dt: float):
    CAMERA_SPEED = 500

    _camera_position = camera_position[:]

    # WASD keys move the entire screen
    if key_handler[pyglet.window.key.W]:
        _camera_position[1] -= CAMERA_SPEED*dt
    if key_handler[pyglet.window.key.A]:
        _camera_position[0] += CAMERA_SPEED*dt
    if key_handler[pyglet.window.key.S]:
        _camera_position[1] += CAMERA_SPEED*dt
    if key_handler[pyglet.window.key.D]:
        _camera_position[0] -= CAMERA_SPEED*dt

    # only update the matrix if we did move
    if camera_position != _camera_position:
        camera_position[:] = _camera_position
        _update_view_matrix()


@display_window.event("on_mouse_scroll")
def handle_camera_zoom(x: int, y: int, scroll_x: float, scroll_y: float):
    # TODO: Zoom in to where the cursor is
    global camera_zoom

    MIN_ZOOM = 0.5
    MAX_ZOOM = 2.0

    new_zoom = camera_zoom + scroll_y
    if new_zoom < MIN_ZOOM or new_zoom > MAX_ZOOM:
        return

    camera_zoom = new_zoom

    _update_view_matrix()


def handle_user_input(dt: float):
    handle_camera_movement(dt)
