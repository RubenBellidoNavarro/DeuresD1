#Arxiu exercici005.py
import pygame
import sys
import utils
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (127, 184, 68)
YELLOW = (240, 187, 64)
ORANGE = (226, 137, 50)
RED = (202, 73, 65)
PURPLE = (135, 65, 152)
BLUE  = (75, 154, 217)
colors = [GREEN, YELLOW, ORANGE, RED, PURPLE, BLUE]

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480), pygame.RESIZABLE)
pygame.display.set_caption('Exercici 005')

mouse = {
    'x': -1,
    'y': -1,
}
font = pygame.font.SysFont('Arial', 20)

def main():
    is_looping = True

    init_game()

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
    return True

def app_run():
    global balloons_explotats
    delta_time = clock.get_time() / 1000

    for balloon in balloons_array:
        update_balloon(balloon, delta_time)
        mouse_sobre_balloon = utils.is_point_in_circle(mouse, balloon['pos'], balloon['radius'])
        if mouse_sobre_balloon:
            init_balloon(balloon)
            balloons_explotats += 1


def app_draw():
    screen.fill(WHITE)

    # Dibujamos recuento de globos
    explotats_text = font.render(f'Caught: {balloons_explotats}', True, BLACK)
    screen.blit(explotats_text, (10, screen.get_height() - 60))
    perduts_text = font.render(f'Caught: {balloons_perduts}', True, BLACK)
    screen.blit(perduts_text, (10, screen.get_height() - 30))

    # Dibujamos los globos
    for balloon in balloons_array:
        pygame.draw.circle(screen, balloon['color'], (balloon['pos']['x'], balloon['pos']['y']), balloon['radius'])

    pygame.display.update()

def init_game():
    global balloons_array, balloons_explotats, balloons_perduts
    balloons_array = []
    balloons_explotats = 0
    balloons_perduts = 0

    for i in range(10):
        balloon = {
            'color': '',
            'radius': 0,
            'pos': {'x': 0, 'y': 0},
            'speed': 0
        }
        init_balloon(balloon)
        balloons_array.append(balloon)
    
def init_balloon(balloon):
    balloon['color'] = random.choice(colors)
    balloon['radius'] = random.randint(5, 15)
    balloon['pos']['y'] = 0
    balloon['pos']['x'] = random.randint(10, screen.get_width() - 10)
    balloon['speed'] = balloon['radius'] * 2 + balloons_explotats

def update_balloon(balloon, delta_time):
    global balloons_perduts
    balloon['pos']['y'] += balloon['speed'] * delta_time
    if balloon['pos']['y'] >= screen.get_height():
        init_balloon(balloon)
        balloons_perduts += 1

if __name__ == '__main__':
    main()