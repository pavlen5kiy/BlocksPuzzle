from simplepbr.shaders import shaders
from ursina import *
from ursina.shaders import *

from classes import *
from settings import *


def create_blue_block(position, scale_x=1, scale_z=1):
    obstacle = BlueBlock(model='cube', color=BLUE_BLOCK_COLOR,
                         position=position, collider='box', scale_x=scale_x,
                         scale_z=scale_z, shader=SHADER)
    return obstacle


def create_pink_block(position, scale_x=1, scale_z=1):
    obstacle = PinkBlock(model='cube', color=PINK_BLOCK_COLOR,
                         position=position, collider='box', scale_x=scale_x,
                         scale_z=scale_z, shader=SHADER)
    return obstacle


def create_white_block(position, scale_x=1, scale_z=1):
    obstacle = WhiteBlock(model='cube', color=WHITE_BLOCK_COLOR,
                          position=position, collider='box', scale_x=scale_x,
                          scale_z=scale_z, shader=SHADER)
    return obstacle


def create_walls():
    walls = [Entity(model='cube', color=WALLS_COLOR,
                    position=Vec3(0, 0, 9.5), scale_x=20, collider='box',
                    shader=SHADER),
             Entity(model='cube', color=WALLS_COLOR,
                    position=Vec3(-5.5, 0, -9.5), scale_x=9, collider='box',
                    shader=SHADER),
             Entity(model='cube', color=WALLS_COLOR,
                    position=Vec3(5.5, 0, -9.5), scale_x=9, collider='box',
                    shader=SHADER),
             Entity(model='cube', color=WALLS_COLOR,
                    position=Vec3(-9.5, 0, 0), scale_z=20, collider='box',
                    shader=SHADER),
             Entity(model='cube', color=WALLS_COLOR,
                    position=Vec3(9.5, 0, 0), scale_z=20, collider='box',
                    shader=SHADER)]
    return walls


def load_level(filename):
    with open(f'levels/{filename}.txt', mode='r') as f:
        return f.read()


def place_player(level_data):
    block_len = 1
    s = '@'
    transposed_level_data = transpose(level_data)

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
                    pos = Vec3(x, 0.03, z + offset)
                    scale_z = block_len
                    return pos, scale_z

                block_len = 1


def place_blue_blocks(level_data):
    res = []
    block_len = 1
    s = 'b'
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
                    res.append(create_blue_block(Vec3(x - offset, 0.01, z), block_len))

                block_len = 1
    return res


def place_pink_blocks(level_data):
    res = []
    block_len = 1
    s = 'p'
    transposed_level_data = transpose(level_data)

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
                    res.append(create_pink_block(Vec3(x, 0.02, z + offset), 1, block_len))

                block_len = 1
    return res

def place_white_blocks(level_data):
    res = []
    for i in range(len(level_data)):
        row = level_data[i]
        for j in range(len(row)):
            curr_s = row[j]
            x = j - 8
            z = 8 - i
            if curr_s == 'w':
                res.append(create_white_block(Vec3(x, 0, z)))
    return res


def transpose(matrix):
    res = []
    for i in range(len(matrix[1])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        res.append(row)
    return res
