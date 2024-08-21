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
