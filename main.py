from PIL.ImageOps import scale
from ursina import *
from ursina.shaders import *

from classes import *
from functions import *
from settings import *

app = Ursina()

window.color = BG_COLOR

camera.rotation = (45, 45, 0)
camera.position = Vec3(-7, 10, -7)
camera.orthographic = True

light = DirectionalLight(shadow_map_resolution=(2048, 2048))
light.rotation = (45, 65, 0)
light.position = Vec3(-18, 23, -18)


def set_level(level):
    restart_hint = Text(text='[R] to restart', scale=0.05, origin=(-2.5, 16),
                        font='fonts/Arial Bold.ttf', color=color.black)
    quit_hint = Text(text='[Q] to quit', scale=0.05, origin=(-3.02, 18),
                     font='fonts/Arial Bold.ttf', color=color.black)
    level_number = Text(text=f'Level {current_level}', scale=0.05,
                        origin=(5, -18),
                        font='fonts/Arial Bold.ttf', color=color.black)

    plane = Entity(model='plane', color=WALLS_COLOR,
                   position=Vec3(0, -0.51, 0), scale=20, shader=SHADER)
    walls = create_walls()

    level_data = load_level(f'level_{level}').split('\n')

    pos, scale_z = place_player(level_data)
    player = Player(model='cube', color=PLAYER_COLOR,
                    position=pos,
                    collider='box', shader=SHADER, scale_z=scale_z)

    place_blue_blocks(level_data)
    place_pink_blocks(level_data)

    for i in range(len(level_data)):
        row = level_data[i]
        for j in range(len(row)):
            curr_s = row[j]
            x = j - 8
            z = 8 - i
            if curr_s == 'w':
                create_white_block(Vec3(x, 0, z))


def input(key):
    global current_level
    if key == 'r':
        scene.clear()
        set_level(current_level)
    if key == 'q':
        quit()


def update():
    global current_level
    hit_info = boxcast(Vec3(0, 0, -11), Vec3(0, 0, 1),
                       distance=0.2, debug=True,
                       thickness=(0.5, 0.5))
    if hit_info.hit:
        if current_level < MAX_LEVEL:
            scene.clear()
            current_level += 1
            set_level(current_level)
        else:
            print('Hey, you\n'
                  'You won dude, ya know\n'
                  'That game is kinda simple btw\n'
                  'Nothing do be proud of')
            quit()


if __name__ == '__main__':
    current_level = 6
    set_level(current_level)
    app.run()
