from ursina import *
from ursina.shaders import *


from classes import *


def create_blue_block(position, scale_x=1, scale_z=1):
    obstacle = BlueBlock(model='cube', color=color.hex('#5560d9'),
                            position=position, collider='box', scale_x=scale_x,
                            scale_z=scale_z)
    return obstacle


def create_pink_block(position, scale_x=1, scale_z=1):
    obstacle = PinkBlock(model='cube', color=color.hex('#ea9cc4'),
                            position=position, collider='box', scale_x=scale_x,
                            scale_z=scale_z)
    return obstacle


def create_white_block(position, scale_x=1, scale_z=1):
    obstacle = WhiteBlock(model='cube', color=color.hex('#ded4d1'),
                          position=position, collider='box', scale_x=scale_x,
                          scale_z=scale_z)
    return obstacle


def create_walls():
    walls = [Entity(model='cube', color=color.hex('#802392'),
                    position=Vec3(0, 0, 9.5), scale_x=20, collider='box',
                    shader=lit_with_shadows_shader),
             Entity(model='cube', color=color.hex('#802392'),
                    position=Vec3(-6, 0, -9.5), scale_x=8, collider='box',
                    shader=lit_with_shadows_shader),
             Entity(model='cube', color=color.hex('#802392'),
                    position=Vec3(6, 0, -9.5), scale_x=8, collider='box',
                    shader=lit_with_shadows_shader),
             Entity(model='cube', color=color.hex('#802392'),
                    position=Vec3(-9.5, 0, 0), scale_z=20, collider='box',
                    shader=lit_with_shadows_shader),
             Entity(model='cube', color=color.hex('#802392'),
                    position=Vec3(9.5, 0, 0), scale_z=20, collider='box',
                    shader=lit_with_shadows_shader)]
    return walls

def load_level(filename):
    with open(f'levels/{filename}.txt', mode='r') as f:
        return f.read()


def place_player(level_data):
    for i in range(len(level_data)):
        row = level_data[i]
        for j in range(len(row)):
            curr_s = row[j]
            x = j - 8
            z = 8 - i
            if curr_s == '@':
                position = Vec3(x, 0, z)
                return position


def place_blue_blocks(level_data):
    block_len = 1
    s = '#'
    for i in range(len(level_data)):
        row = level_data[i]
        for j in range(len(row)):

            x = j - 8
            z = 8 - i

            curr_s = row[j]
            next_s = row[j + 1] if j < 16 else ''

            offset = 0.5 * (block_len - 1)

            if curr_s == next_s == s:
                block_len += 1
            else:
                if curr_s == s:
                    create_blue_block(Vec3(x - offset, 0, z), block_len)

                block_len = 1


def place_pink_blocks(level_data):
    block_len = 1
    s = '%'
    transposed_level_data = transpose(level_data)
    for row in transposed_level_data:
        print(''.join(row))

    for i in range(len(transposed_level_data)):
        row = transposed_level_data[i]
        for j in range(len(row)):

            x = i - 8
            z = 8 - j

            curr_s = row[j]
            next_s = row[j + 1] if j < 16 else ''

            offset = 0.5 * (block_len - 1)

            if curr_s == next_s == s:
                block_len += 1
            else:
                if curr_s == s:
                    create_pink_block(Vec3(x, 0, z + offset), 1, block_len)

                block_len = 1

def transpose(matrix):
    res = []
    for i in range(len(matrix[1])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        res.append(row)
    return res
