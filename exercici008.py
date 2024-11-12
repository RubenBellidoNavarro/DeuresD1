#Arxiu exercici008.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (100, 200, 255)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 008')

BUTTON_SIZE = 50
PADDING = 50

buttons = [
    {
    'x': PADDING,
    'y': PADDING,
    'width': BUTTON_SIZE,
    'height': BUTTON_SIZE,
    'state': 'pressed'
    },
    {
    'x': PADDING,
    'y': PADDING + BUTTON_SIZE,
    'width': BUTTON_SIZE,
    'height': BUTTON_SIZE,
    'state': 'none'
    }
]

mouse = {
    'x': -1,
    'y': -1,
    'clicked': False
}

circle = {
    'x': int(screen.get_width() / 2),
    'y': int(screen.get_height() / 2),
    'radius': 30,
    'color': BLUE,
    'speed': 150
}

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
                if button['state'] == 'clicked':
                    if i == 0:
                        button['state'] = 'pressed'
                        buttons[1]['state'] = 'none'
                    if i == 1:
                        buttons[0]['state'] = 'none'
                        button['state'] = 'pressed'
            mouse['clicked'] = False
    return True

def app_run():
    global circle
    # Comprobamos si se está clickando un botón
    for button in buttons:
        if button['state'] != 'pressed':
            mouse_sobre_button = utils.is_point_in_rect(mouse, button)
            if mouse_sobre_button and mouse['clicked']:
                button['state'] = 'clicked'
            else:
                button['state'] = 'none'

    # Actualizamos posición circulo en función de botón pulsado
    delta_time = clock.get_time() / 1000
    for i, button in enumerate(buttons):
        if button['state'] == 'pressed':
            if i == 0:
                circle['y'] -= circle['speed'] * delta_time
                if circle['y'] <= circle['radius']:
                    circle['y'] = circle['radius']                    
            elif i == 1:
                circle['y'] += circle['speed'] * delta_time
                if circle['y'] >= screen.get_height() - circle['radius']:
                    circle['y'] = screen.get_height() - circle['radius']

def app_draw():
    screen.fill(WHITE)

    # Dibujamos botones
    for button in buttons:
        draw_button(button)

    # Dibujamos circulo
    center = (circle['x'], circle['y'])
    pygame.draw.circle(screen, circle['color'], center, circle['radius'])

    # Dibujamos texto indicando ratón pulsado
    if mouse['clicked']:
        mouse_pressed_text = font.render('Mouse Pressed', True, BLACK)
        pos_text = (PADDING + BUTTON_SIZE + 5, PADDING + 5)
        screen.blit(mouse_pressed_text, pos_text)

    pygame.display.update()

def draw_button(button):
    rect_values = (button['x'], button['y'], BUTTON_SIZE, BUTTON_SIZE)
    if button['state'] != 'none':
        if button['state'] == 'pressed':
            color = BLUE
        elif button['state'] == 'clicked':
            color = ORANGE
        pygame.draw.rect(screen, color, rect_values)
    pygame.draw.rect(screen, BLACK, rect_values, 2)

if __name__ == '__main__':
    main()