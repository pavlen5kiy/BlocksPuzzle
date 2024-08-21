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
                position=Vec3(0, 0, 8),
                collider='box', shader=lit_with_shadows_shader)

plane = Entity(model='plane', color=color.hex('#802392'),
               position=Vec3(0, -0.51, 0), scale=20)
walls = create_walls()

level_data = load_level('level').split('\n')

for i in range(len(level_data)):
    row = level_data[i]
    for j in range(len(row)):
        curr_s = row[j]
        x = j - 8
        z = 8 - i
        if curr_s == '@':
            player.position = Vec3(x, 0, z)
        elif curr_s == '#':
            create_blue_block(Vec3(x, 0, z))
        elif curr_s == '%':
            create_pink_block(Vec3(x, 0, z))
        elif curr_s == '&':
            create_white_block(Vec3(x, 0, z))



if __name__ == '__main__':
    app.run()
