#Arxiu exercici006.py
import pygame
import sys
import utils
import random
from assets.svgmoji.emojis import get_emoji

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 200, 255)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480), pygame.RESIZABLE)
pygame.display.set_caption('Exercici 006')

mouse = {
    'x': -1,
    'y': -1,
    }
window_size = {
    'width': screen.get_width(),
    'height': screen.get_height(),
    'center': {'x': int(screen.get_width() / 2), 'y': int(screen.get_height() / 2)}
}

CELL_SIZE = 50
ROWS = 8
COLS = 12

img_ship = get_emoji(pygame, "🚢", size=CELL_SIZE)
img_water = get_emoji(pygame, "🌊", size=CELL_SIZE)
img_bomb = get_emoji(pygame, "💥", size=CELL_SIZE)

board = []
board_pos = {'x': -1, 'y': -1}

def main():
    is_looping = True

    init_board()

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60)

    pygame.quit()
    sys.exit()

def app_events():
    global mouse
    mouse_inside = pygame.mouse.get_focused()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse['x'] = event.pos[0]
                mouse['y'] = event.pos[1]
            else:
                mouse['x'] = -1
                mouse['y'] = -1

        elif event.type == pygame.MOUSEBUTTONDOWN:
            cell_x = int((mouse["x"] - board_pos["x"]) / CELL_SIZE)
            cell_y = int((mouse["y"] - board_pos["y"]) / CELL_SIZE)
            if 0 <= cell_x < len(board[0]) and 0 <= cell_y < len(board):
                if board[cell_y][cell_x] == "":
                    board[cell_y][cell_x] = "W"
                elif board[cell_y][cell_x] == "S":
                    board[cell_y][cell_x] = "B"

    return True

def app_run():
    global window_size, board_pos
    # Calculamos posición tablero y tamaño pantalla
    window_size["width"] = screen.get_width()
    window_size["height"] = screen.get_height()
    window_size["center"]["x"] = int(screen.get_width() / 2)
    window_size["center"]["y"] = int(screen.get_height() / 2)

    board_pos["x"] = window_size["center"]["x"] - int(len(board[0]) * CELL_SIZE / 2)
    board_pos["y"] = window_size["center"]["y"] - int(len(board) * CELL_SIZE / 2)

def app_draw():
    screen.fill(WHITE)

    # Dibujamos tablero
    draw_board()

    pygame.display.update()

def init_board():
    global board
    
    # Iniciamos tablero vacío
    board = []
    for x in range(ROWS):
        row = []
        for y in range(COLS):
            row.append('')
        board.append(row)

    # Ponemos barcos en tablero
    barcos = ((3, 'horizontal'), (4, 'horizontal'), (3, 'vertical'))
    for grupo_barcos in barcos:
        length = grupo_barcos[0]
        direction = grupo_barcos[1]

        posicio_valida = False
        while not posicio_valida:
            x = random.randint(0, ROWS - 1)
            y = random.randint(0, COLS - 1)
            posicio_valida = is_valid_position(x, y, length, direction)
        
        place_ship(x, y, length, direction)

def draw_board():
    for i in range(ROWS):
        for j in range(COLS):

            cell_x = board_pos['x'] + j * CELL_SIZE
            cell_y = board_pos['y'] + i * CELL_SIZE
            rect_values = (cell_x, cell_y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLUE, rect_values)

            if board[i][j] == 'S':
                screen.blit(img_ship, (cell_x, cell_y))
            elif board[i][j] == 'W':
                screen.blit(img_water, (cell_x, cell_y))
            elif board[i][j] == 'B':
                screen.blit(img_ship, (cell_x, cell_y))
                screen.blit(img_bomb, (cell_x, cell_y))

def place_ship(x, y, length, direction):
    global board
    if direction == 'horizontal':
        for j in range(length):
            board[x][y + j] = 'S'
    elif direction == 'vertical':
        for i in range(length):
            board[x + i][y] = 'S'

def is_valid_position(x, y, length, direction):

    # Comprobamos que todos los barcos no salgan del tablero
    if direction == 'horizontal' and y + length <= COLS:
        # Comprobamos los espacios que ocuparían los barcos, la fila superior y la inferior:
        for j in range(length):
            if board[x][y + j] != '':
                return False
            if x > 0 and board[x - 1][y + j] != '':
                return False
            if x < ROWS - 1 and board[x + 1][y + j] != '':
                return False
        # Comprobamos las casillas laterales a los barcos:
        if y > 0 and board[x][y - 1] != '':
            return False
        if y + length < COLS and board[x][y + length] != '':
            return False
        return True
        
    elif direction == 'vertical' and x + length <= ROWS:
        for i in range(length):
            if board[x + i][y] != '':
                return False
            if y > 0 and board[x + i][y - 1] != '':
                return False
            if y < COLS - 1 and board[x + i][y + 1] != '':
                return False
        if x > 0 and board[x - 1][y] != '':
            return False
        if x + length < ROWS and board[x + length][y] != '':
            return False
        return True
    
    return False

if __name__ == '__main__':
    main()