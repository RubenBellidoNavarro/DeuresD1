#Arxiu exercici003.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480), pygame.RESIZABLE)
pygame.display.set_caption('Exercici 003')

rect = {
    'color': BLUE,
    'pos': {'x': 50, 'y': 50},
    'SIZE': 40
}

mouse_pos = {
    'x': 0,
    'y': 0
}

PADDING = 50
THICK = 3

def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60)

    pygame.quit()
    sys.exit()

def app_events():
    global mouse_pos
    mouse_inside = pygame.mouse.get_focused() # Devuelve True si el ratón está dentro de la pantalla
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEMOTION:
            # TODO Si el ratón no está dentro de la pantalla, no actualizamos la posición
            if mouse_inside:
                mouse_pos['x'] = event.pos[0]
                mouse_pos['y'] = event.pos[1]
    return True

def app_run():
    global rect
    # TODO Actualizamos posición rectángulo
    rect['pos']['x'] = mouse_pos['x'] - (rect['SIZE'] / 2)
    rect['pos']['y'] = mouse_pos['y'] - (rect['SIZE'] / 2)
    
    # TODO Calculamos rectángulos que delimitan regiones
    width = screen.get_width() / 2 - PADDING # Es igual en las 4 regiones
    height = screen.get_height() / 2 - PADDING # Es igual en las 4 regiones
    rect_vermell = {'x':PADDING, 'y':PADDING, 'width':width, 'height':height}
    rect_blau = {'x':screen.get_width() / 2, 'y':PADDING, 'width':width, 'height':height}
    rect_verd = {'x':PADDING, 'y':screen.get_height() / 2, 'width':width, 'height':height}
    rect_groga = {'x':screen.get_width() / 2, 'y':screen.get_height() / 2, 'width':width, 'height':height}
    
    # TODO Asignamos color en función de la región
    if utils.is_point_in_rect(mouse_pos, rect_vermell):
        rect['color'] = RED
    elif utils.is_point_in_rect(mouse_pos, rect_blau):
        rect['color'] = BLUE
    elif utils.is_point_in_rect(mouse_pos, rect_verd):
        rect['color'] = GREEN
    elif utils.is_point_in_rect(mouse_pos, rect_groga):
        rect['color'] = YELLOW
    else:
        rect['color'] = BLACK

def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    # Dibujamos límite línea vértical
    starting_point = (screen.get_width() / 2, 0)
    ending_point = (starting_point[0], screen.get_height())
    pygame.draw.line(screen, BLACK, starting_point, ending_point, THICK)

    # Dibujamos límite linea horizontal
    starting_point = (0, screen.get_height() / 2)
    ending_point = (screen.get_width(), starting_point[1])
    pygame.draw.line(screen, BLACK, starting_point, ending_point, THICK)

    # Dibujamos límite rectangular
    rect_values = (PADDING, PADDING, screen.get_width() - PADDING * 2, screen.get_height() - PADDING * 2)
    pygame.draw.rect(screen, BLACK, rect_values, THICK)

    # Dibujamos rectángulo
    rect_values = (rect['pos']['x'], rect['pos']['y'], rect['SIZE'], rect['SIZE'])
    pygame.draw.rect(screen, rect['color'], rect_values)
    pygame.draw.rect(screen, BLACK, rect_values, 1)

    pygame.display.update()

if __name__ == '__main__':
    main()