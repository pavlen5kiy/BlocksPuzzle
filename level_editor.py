import pygame
import copy

from functions import load_level
from settings import theme, COLORS

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['.'] * width for _ in range(height)]
        self.board[0][8] = '@'

        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        colors = {'.': pygame.Color(f'#{COLORS["walls"][theme]}'),
                  '@': pygame.Color(f'#{COLORS["player"][theme]}'),
                  'b': pygame.Color(f'#{COLORS["blue_block"][theme]}'),
                  'p': pygame.Color(f'#{COLORS["pink_block"][theme]}'),
                  'w': pygame.Color(f'#{COLORS["white_block"][theme]}')}

        border = pygame.Color('white')

        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, colors[self.board[y][x]], (
                    x * self.cell_size + self.left,
                    y * self.cell_size + self.top,
                    self.cell_size, self.cell_size))
                pygame.draw.rect(screen, border, (
                    x * self.cell_size + self.left,
                    y * self.cell_size + self.top,
                    self.cell_size, self.cell_size), 1)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or \
                cell_y < 0 or cell_x >= self.height:
            return
        return cell_x, cell_y

    def on_click(self, cell, mode, drawing=False, erase=False):
        if drawing:
            self.board[cell[1]][cell[0]] = mode
        elif erase:
            self.board[cell[1]][cell[0]] = '.'

    def get_click(self, mouse_pos, mode, drawing=False, erase=False):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell, mode, drawing, erase)


def main():
    clock = pygame.time.Clock()
    pygame.init()
    size = 850, 850

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Level Editor')

    cell_size = 50
    left = 0
    top = 0
    width, height = size[0] // cell_size, size[1] // cell_size

    board = Board(width, height)
    default = [['.'] * width for _ in range(height)]
    board.set_view(left, top, cell_size)

    running = True
    drawing = False
    erase = False

    level_number = 5

    mode = 'b'

    fps = 30

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board.board = copy.deepcopy(default)
                    board.board[0][8] = '@'
                if event.key == pygame.K_b:
                    mode = 'b'
                if event.key == pygame.K_p:
                    mode = 'p'
                if event.key == pygame.K_w:
                    mode = 'w'
                if event.key == pygame.K_a:
                    mode = '@'

                if event.key == pygame.K_s:
                    data = ''
                    for i in range(len(board.board)):
                        if i < len(board.board) - 1:
                            data += ''.join(board.board[i]) + '\n'
                        else:
                            data += ''.join(board.board[i])
                    with open(f'levels/level_{input("Save level as (number of level): ")}.txt', mode='w') as f:
                        f.write(data)
                    level_number += 1

                if event.key == pygame.K_o:
                    data = []
                    for row in load_level(f'level_{input("Edit level (number of level): ")}').split('\n'):
                        r = [s for s in row]
                        data.append(r)
                    board.board = data

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    board.get_click(event.pos, mode, drawing)
                elif event.button == 3:
                    erase = True
                    board.get_click(event.pos, mode, erase=erase)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                elif event.button == 3:
                    erase = False
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    x, y = event.pos
                    board.get_click(event.pos, mode, drawing)
                elif erase:
                    x, y = event.pos
                    board.get_click(event.pos, mode, erase=erase)

        screen.fill((0, 0, 0))
        board.render(screen)

        clock.tick(fps)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
