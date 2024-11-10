#Arxiu exercici000.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 000')

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def app_run():
    pass

def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    center = {'x': 100, 'y': 225}
    for cnt in range(0,10):
        radius = 10 + cnt * 2.5
        pygame.draw.circle(screen, GRAY, tuple(center.values()), radius)
        pygame.draw.circle(screen, BLUE, tuple(center.values()), radius, 3)
        center['x'] += 50

    pygame.display.update()

if __name__ == '__main__':
    main()