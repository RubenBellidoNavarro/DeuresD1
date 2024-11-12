#Arxiu exercici007.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480), pygame.RESIZABLE)
pygame.display.set_caption('Exercici 007')

WIDTH_BUTTON = 50
HEIGHT_BUTTON = 20
PADDING = 20

buttons = [
    {
    'x': PADDING,
    'y': PADDING,
    'clicked': False
    },
    {
    'x': PADDING + WIDTH_BUTTON,
    'y': PADDING,
    'clicked': False
    }
]

valor = 0

mouse = {
    'x': -1,
    'y': -1,
    'clicked': False
}

window_size = {
    'width': screen.get_width(),
    'height': screen.get_height(),
    'center': {
        'x': int(screen.get_width() / 2),
        'y': int(screen.get_height() / 2)
    }
}

font_petita = pygame.font.SysFont('Arial', 15)
font_gran = pygame.font.SysFont('Arial', 40)
mouse_pressed_text = font_petita.render('Mouse Pressed', True, BLACK)


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
    global mouse, valor
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
            if mouse_inside:
                mouse['clicked'] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for i, button in enumerate(buttons):
                if button['clicked']:
                    if i == 0:
                        valor -= 1
                    elif i == 1:
                        valor += 1
            mouse['clicked'] = False
    return True

def app_run():
    global window_size, buttons
    # Calculamos tamaño ventana
    window_size['width'] = screen.get_width()
    window_size['height'] = screen.get_height()
    window_size['center']['x'] = int(screen.get_width() / 2)
    window_size['center']['y'] = int(screen.get_height() / 2)

    # Comprobamos si algún pulsador está siendo clickado
    for button in buttons:
        rect_button = {'x': button['x'], 'y': button['y'], 'width': WIDTH_BUTTON, 'height': HEIGHT_BUTTON}
        if mouse['clicked'] and utils.is_point_in_rect(mouse, rect_button):
            button['clicked'] = True
        else:
            button['clicked'] = False

def app_draw():
    screen.fill(WHITE)

    # Dibujamos los pulsadores
    for button in buttons:
        draw_button(button)

    # Dibujamos indicador de ratón clickado
    if mouse['clicked']:
        x = PADDING + 2 * WIDTH_BUTTON + 10
        y = PADDING
        screen.blit(mouse_pressed_text, (x, y))
    
    # Dibujamos el valor en el centro de la pantalla
    draw_value()

    pygame.display.update()

def draw_button(button):
    # Dibujamos rectángulo
    rect_values = (button['x'], button['y'], WIDTH_BUTTON, HEIGHT_BUTTON)
    if button['clicked']:
        pygame.draw.rect(screen, ORANGE, rect_values)
    pygame.draw.rect(screen, BLACK, rect_values, 2)

    # Dibujamos signo
    sign = '+'
    if button is buttons[0]:
        sign = '-'
    sign_text = font_petita.render(sign, True, 10)
    sign_rect = sign_text.get_rect()
    sign_rect.centerx = int(button['x'] + WIDTH_BUTTON / 2)
    sign_rect.centery = int(button['y'] + HEIGHT_BUTTON / 2)
    screen.blit(sign_text, sign_rect)

def draw_value():
    valor_surface = font_gran.render(str(valor), True, BLACK)
    valor_rect = valor_surface.get_rect()
    valor_rect.centerx = window_size['center']['x']
    valor_rect.centery = window_size['center']['y']
    screen.blit(valor_surface, valor_rect)

if __name__ == '__main__':
    main()