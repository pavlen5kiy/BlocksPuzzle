from ursina import color
from ursina.shaders import *

SPEED = 10

SHADER = lit_with_shadows_shader

MAX_LEVEL = 7

BOXCAST_THICKNESS = 0.9
BOXCAST_DISTANCE = 0.5
BOXCAST_DISTANCE_MODIFIER = 0.1

theme = 3
COLORS = {
    'white_block': ['ded4d1', 'e3cfb4', 'ffeced', 'dee6c1', 'ebe3cc', 'dfe6e0'],
    'blue_block': ['5560d9', '243d5c', 'a8b5ae', '707a8a', '162944', '7687ab'],
    'pink_block': ['ea9cc4', 'b03a48', 'f1b4b4', 'd18293', '713a29', 'c17b5c'],
    'player': ['a1ff71', '3e6958', 'cac18a', '7a9c6b', '565c56', '596e47'],
    'bg': ['b3daee', '5c8b93', 'e2e4df', '707a8a', 'fbe5c9', 'a9bbcc'],
    'walls': ['802392', 'b1a58d', '92929c', '4c4961', 'b7a182', 'd9c277'],
}

BLUE_BLOCK_COLOR = color.hex(f'#{COLORS["blue_block"][theme]}')
PINK_BLOCK_COLOR = color.hex(f'#{COLORS["pink_block"][theme]}')
WHITE_BLOCK_COLOR = color.hex(f'#{COLORS["white_block"][theme]}')
WALLS_COLOR = color.hex(f'#{COLORS["walls"][theme]}')
PLAYER_COLOR = color.hex(f'#{COLORS["player"][theme]}')
BG_COLOR = color.hex(f'#{COLORS["bg"][theme]}')
