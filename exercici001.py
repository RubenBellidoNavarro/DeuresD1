#Arxiu exercici001.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 001')

window_size = { 
    "width": 0, 
    "height": 0, 
    "center": {
        "x": 0,
        "y": 0
    } 
}

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
    global window_size
    window_size["width"] = screen.get_width()
    window_size["height"] = screen.get_height()
    window_size["center"]["x"] = int(screen.get_width() / 2)
    window_size["center"]["y"] = int(screen.get_height() / 2)

def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    for q in range(20, 0, -1):
        perspective = (q / 20)
        q_ample = q * 25 * perspective
        q_alt = q * 20 * perspective
        x = window_size["center"]["x"] - (q_ample / 2)
        y = window_size["center"]["y"] - (q_alt / 2)
        color = (0, q * 10, 0)
        if q % 2 == 0:
            color = (0, 0, q * 10)
        pygame.draw.rect(screen, color, (x, y, q_ample, q_alt))

    pygame.display.update()

if __name__ == '__main__':
    main()