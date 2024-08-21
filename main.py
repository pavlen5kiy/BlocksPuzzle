from ursina import *
from ursina.shaders import *

from classes import *
from functions import *

app = Ursina()

window.color = color.hex('#b3daee')

camera.rotation = (45, 45, 0)
camera.position = Vec3(-7, 10, -7)
camera.orthographic = True

light = DirectionalLight(shadow_map_resolution=(2048, 2048))
light.rotation = (45, 65, 0)
light.position = Vec3(-18, 23, -18)

player = Player(model='cube', color=color.hex('#a1ff71'),
                position=Vec3(0, 0, 5),
                collider='box', shader=lit_with_shadows_shader)

plane = Entity(model='plane', color=color.hex('#802392'),
               position=Vec3(0, -0.51, 0), scale=20)
walls = create_walls()

obstacles = [create_z_movable_obst(Vec3(1, 0, -2), 1, 1),
             create_x_movable_obst(Vec3(3, 0, 3), 1, 1),
             create_static_obst(Vec3(4, 0, 4))]

if __name__ == '__main__':
    app.run()
