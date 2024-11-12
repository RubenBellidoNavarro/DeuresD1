#Arxiu exercici009.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (100, 200, 255)
RED = (255, 0, 0)
GRAY = (215, 215, 215)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 009')

PADDING = 40
BUTTON_SIZE = 40

mouse = {
    'x': -1,
    'y': -1,
    'clicked': False
}

def main():
    is_looping = True

    init_buttons()

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60)

    pygame.quit()
    sys.exit()

def app_events():
    global mouse, buttons
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
            for button in buttons:
                if button['state'] == 'clicked':
                    button['state'] = 'pressed'
                    break
                elif button['state'] == 'pressed' and utils.is_point_in_rect(mouse, button):
                    button['state'] = 'none'
                    break
            mouse['clicked'] = False

    return True

def app_run():
    global buttons, valor
    # Comprobamos si se está clickando un botón
    for button in buttons:
        if button['state'] != 'pressed':
            if utils.is_point_in_rect(mouse, button) and mouse['clicked']:
                button['state'] = 'clicked'
            else:
                button['state'] = 'none'

    # Calculamos el valor decimal en función de los botones apretados
    tmp = 0
    for button in buttons:
        if button['state'] == 'clicked' or button['state'] == 'pressed':
            tmp += 2 ** button['number']
    valor = tmp

def app_draw():
    screen.fill(WHITE)

    # Dibujamos botones
    for button in buttons:
        draw_button(button)

    # Dibujamos dígitos
    draw_digit()

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

def init_buttons():
    global buttons
    buttons = []
    n_buttons = 4

    for i in range(n_buttons):
        button = {
            'x': PADDING + BUTTON_SIZE * i,
            'y': PADDING,
            'width': BUTTON_SIZE,
            'height': BUTTON_SIZE,
            'state': 'none',
            'number': n_buttons - 1 - i
        }
        buttons.append(button)

def draw_digit():
    center_x = int(screen.get_width() / 2)
    center_y = int(screen.get_height() / 2)
    long_segment = 50
    '''
    PUNTOS QUE UNEN LOS SEGMENTOS:

    1---4
    |   |
    2---5
    |   |
    3---6
    '''
    # Calculamos coordenadas para cada punto
    x_123 = center_x - int(long_segment / 2)
    x_456 = center_x + int(long_segment / 2)
    y_14 = center_y - long_segment
    y_25 = center_y
    y_36 = center_y + long_segment

    # Creamos estructura para segmentos
    segments = {
       '14': {'punt_inici': {'x': x_123, 'y': y_14}, 'punt_final': {'x': x_456, 'y': y_14}, 'color': GRAY},
       '12': {'punt_inici': {'x': x_123, 'y': y_14}, 'punt_final': {'x': x_123, 'y': y_25}, 'color': GRAY},
       '45': {'punt_inici': {'x': x_456, 'y': y_14}, 'punt_final': {'x': x_456, 'y': y_25}, 'color': GRAY},
       '25': {'punt_inici': {'x': x_123, 'y': y_25}, 'punt_final': {'x': x_456, 'y': y_25}, 'color': GRAY},
       '23': {'punt_inici': {'x': x_123, 'y': y_25}, 'punt_final': {'x': x_123, 'y': y_36}, 'color': GRAY},
       '56': {'punt_inici': {'x': x_456, 'y': y_25}, 'punt_final': {'x': x_456, 'y': y_36}, 'color': GRAY},
       '36': {'punt_inici': {'x': x_123, 'y': y_36}, 'punt_final': {'x': x_456, 'y': y_36}, 'color': GRAY},
    }

    # Asignamos colores a cada segmento en función del valor guardado
    relacion_valor_color = [
        {'valor': 0, 'segments_vermells': ('12','23','36','56','45','14')},
        {'valor': 1, 'segments_vermells': ('45','56')},
        {'valor': 2, 'segments_vermells': ('14','23','25','36','45')},
        {'valor': 3, 'segments_vermells': ('14','25','36','45','56')},
        {'valor': 4, 'segments_vermells': ('12','25','45','56')},
        {'valor': 5, 'segments_vermells': ('12','14','25','36','56')},
        {'valor': 6, 'segments_vermells': ('12','14','23','25','36','56')},
        {'valor': 7, 'segments_vermells': ('14','45','56')},
        {'valor': 8, 'segments_vermells': ('12','14','23','25','36','45','56')},
        {'valor': 9, 'segments_vermells': ('12','14','25','36','45','56')},
        {'valor': 10, 'segments_vermells': ('14','23','25','36','45','56')},
        {'valor': 11, 'segments_vermells': ('12','23','25','36','56')},
        {'valor': 12, 'segments_vermells': ('23','25','36')},
        {'valor': 13, 'segments_vermells': ('23','25','36','45','56')},
        {'valor': 14, 'segments_vermells': ('12','14','23','25','36','45')},
        {'valor': 15, 'segments_vermells': ('12','14','23','25')},
    ]

    for relacion in relacion_valor_color:
        if relacion['valor'] == valor:
            for segment in segments:
                if segment in relacion['segments_vermells']:
                    segments[segment]['color'] = RED
            break

    # Dibujamos segmentos
    thickness = 6
    for segment in segments:
        punt_inici = tuple(segments[segment]['punt_inici'].values())
        punt_final = tuple(segments[segment]['punt_final'].values())
        color = segments[segment]['color']
        pygame.draw.line(screen, color, punt_inici, punt_final, thickness)
    
    # Dibujamos de blanco los puntos que unen los segmentos
    x_array = [x_123, x_456]
    y_array = [y_14, y_25, y_36]
    for x in x_array:
        for y in y_array:
            x_rect = x
            y_rect = y
            # Definimos un objeto Rect, para poder asignarle un centerx y un centery
            rect_values = pygame.Rect(x_rect, y_rect, thickness, thickness)
            rect_values.centerx = x_rect + 1
            rect_values.centery = y_rect + 1
            pygame.draw.rect(screen, WHITE, rect_values)
    

if __name__ == '__main__':
    main()