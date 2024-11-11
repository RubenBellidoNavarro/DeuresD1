#Arxiu exercici002.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 002')

font = pygame.font.SysFont('Arial', 20)

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

    pygame.draw.circle(screen, BLUE, (100, 50), 5)
    draw_text("Poma", font, 100, 50, "left", "bottom")

    pygame.draw.circle(screen, BLUE, (100, 100), 5)
    draw_text("Pera", font, 100, 100, "center", "center")

    pygame.draw.circle(screen, BLUE, (100, 150), 5)
    draw_text("Raïm", font, 100, 150, "right", "top")

    pygame.draw.circle(screen, BLUE, (250, 50), 5)
    draw_text("Plàtan", font, 250, 50, "left", "top")

    pygame.draw.circle(screen, BLUE, (250, 100), 5)
    draw_text("Préssec", font, 250, 100, "center", "center")
    
    pygame.draw.circle(screen, BLUE, (250, 150), 5)
    draw_text("Maduixa", font, 250, 150, "right", "bottom")

    pygame.display.update()

def draw_text(text, font, x, y, align_x="left", align_y="top"):
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()

    if align_x == 'left':
        text_rect.left = x
    elif align_x == 'center':
        text_rect.centerx = x
    elif align_x == 'right':
        text_rect.right = x

    if align_y == 'top':
        text_rect.top = y
    elif align_y == 'center':
        text_rect.centery = y
    elif align_y == 'bottom':
        text_rect.bottom = y

    screen.blit(text_surface, text_rect)

if __name__ == '__main__':
    main()