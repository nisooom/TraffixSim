
from src.common import display_window, key_handler, mouse_handler, camera_attrs
import pyglet


def _update_view_matrix():
    view_mat = pyglet.math.Mat4()
    view_mat = view_mat.translate(camera_attrs['position'])
    view_mat = view_mat.scale([camera_attrs['scale'], camera_attrs['scale'], 1])
    display_window.view = view_mat

_update_view_matrix()


def handle_camera_movement(dt: float):
    CAMERA_SPEED = 500

    _camera_position = camera_attrs['position'][:]

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
    if camera_attrs['position'] != _camera_position:
        camera_attrs['position'][:] = _camera_position
        _update_view_matrix()


@display_window.event("on_mouse_scroll")
def handle_camera_zoom(x: int, y: int, scroll_x: float, scroll_y: float):
    # TODO: Zoom in to where the cursor is

    MIN_ZOOM = 0.8
    MAX_ZOOM = 4.0

    new_zoom = camera_attrs['scale'] + scroll_y
    new_zoom = pyglet.math.clamp(new_zoom, MIN_ZOOM, MAX_ZOOM)

    camera_attrs['scale'] = new_zoom

    _update_view_matrix()


def handle_user_input(dt: float):
    handle_camera_movement(dt)
