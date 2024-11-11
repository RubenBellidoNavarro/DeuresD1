#Arxiu exercici004.py
import pygame
import sys
import utils
import random

WHITE = (255, 255, 255)
GREEN = (127, 184, 68)
YELLOW = (240, 187, 64)
ORANGE = (226, 137, 50)
RED = (202, 73, 65)
PURPLE = (135, 65, 152)
BLUE  = (75, 154, 217)
colors = [GREEN, YELLOW, ORANGE, RED, PURPLE, BLUE]

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 004')

array_globos = []
mouse_pos = {'x': -1, 'y':-1}
mouse_clicked = False

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
    global mouse_pos, mouse_clicked
    mouse_inside = pygame.mouse.get_focused() # Devuelve True si el ratón está dentro de la pantalla
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos['x'] = event.pos[0]
                mouse_pos['y'] = event.pos[1]
            else:
                mouse_pos['x'] = -1
                mouse_pos['y'] = -1
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_clicked = True
    return True

def app_run():
    global mouse_clicked
    delta_time = clock.get_time() / 1000
    speed = 5
    delta_radius = speed * delta_time

    # TODO Actualiza los radios de los globos de la lista (la lista debe tener al menos 1 globo)
    if len(array_globos) >= 1:
        for globo in array_globos:
            if globo['radius'] >= 5:
                globo['radius'] -= delta_radius
            else:
                globo['radius'] = 5

    # TODO Si se hace click, se añade un globo y se modifica 'mouse_clicked'
    if mouse_clicked:
        afegeix_globo()
        mouse_clicked = False

def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    # TODO Dibujamos los globos en pantalla
    for globo in array_globos:
        center = (globo['pos']['x'], globo['pos']['y'])
        pygame.draw.circle(screen, globo['color'], center, globo['radius'])

    pygame.display.update()

def afegeix_globo():
    global array_globos
    color = random.choice(colors)
    dict_globo = {
        'color': color,
        'radius': 25,
        'pos': {'x': mouse_pos['x'], 'y': mouse_pos['y']}}
    array_globos.append(dict_globo)

if __name__ == '__main__':
    main()