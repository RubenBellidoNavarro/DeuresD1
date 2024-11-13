#Arxiu exercici010.py
import pygame
import sys
import utils
import math
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480), pygame.RESIZABLE)
pygame.display.set_caption('Exercici 010')


mouse_pos = {
    'x': screen.get_width() // 2,
    'y': screen.get_height() // 2
}

snake = {
    "queue": [],
    "speed": 50,
    "radius": 7,
    "status": "follow_mouse", # "follow_mouse" or "orbit_mouse"
    "direction_angle": 0
}

piece = { # (food)
    "x": -1, 
    "y": -1, 
    "value": 0,
    "radius": 7
}

font_piece = pygame.font.SysFont('Arial', 8)
font_board = pygame.font.SysFont('Arial', 15)

level = 1

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
    global mouse, valor
    mouse_inside = pygame.mouse.get_focused()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos['x'] = event.pos[0]
                mouse_pos['y'] = event.pos[1]
    return True

def app_run():
    # Actualizamos posición serpiente
    delta_time = clock.get_time() / 1000
    move_snake(delta_time)

def app_draw():
    screen.fill(WHITE)

    # Dibujamos poma
    draw_piece()

    # Dibujamos serpiente
    draw_snake()

    # Dibujamos stats partida
    draw_board()

    pygame.display.update()

def init_game():
    # Inicia el joc creant la primera peça si no existeix i col·locant la serp al centre de la pantalla amb una mida inicial de 5 segments.
    global snake

    # Iniciamos poma
    generate_piece()

    # Iniciamos serpiente
    circle_pos = {'x': screen.get_width() // 2, 'y': screen.get_height() // 2}
    for i in range(5):
        snake["queue"].append(circle_pos)

def generate_piece():
    # Genera una nova peça amb una posició i un valor aleatori dins dels límits de la finestra.
    global piece
    padding = 100
    piece["x"] = random.randint(padding, screen.get_width() - padding)
    piece["y"] = random.randint(padding, screen.get_height() - padding)
    piece['value'] = random.randint(1,4)
    

def extend_snake():
    # Afegeix un segment addicional a la cua de la serp copiant l'última posició de la cua actual.
    global snake
    ultim_element = snake["queue"][-1]
    snake["queue"].append(ultim_element)

def move_snake(delta_time):
    # Detecta si la serp ha xocat amb la peça, augmenta la velocitat i la longitud de la serp segons el valor de la peça, i genera una nova peça si cal. Calcula i actualitza la nova posició del cap de la serp i elimina l'últim segment per mantenir la longitud constant.
    
    global snake, level
    # Detectamos si serpiente colisiona con poma
    posicion_poma = {'x': piece["x"], 'y': piece["y"]}
    posicion_cabeza_sepiente = snake['queue'][0]
    delta_x = abs(posicion_poma['x'] - posicion_cabeza_sepiente['x'])
    delta_y = abs(posicion_poma['y'] - posicion_cabeza_sepiente['y'])
    distancia = math.sqrt(delta_x ** 2 + delta_y ** 2) # Teorema de Pitágoras
    serpiente_toca_poma = distancia <= (snake['radius'] + piece["radius"])
    if serpiente_toca_poma:
        # Modificamos velocidad
        snake['speed'] *= 1.05
        if snake['speed'] > 200:
            snake["speed"] = 200

        # Añadimos segmentos serpiente
        n_segmentos = piece["value"]
        ultimo_segmento = snake['queue'][-1]
        for i in range(n_segmentos):
            snake['queue'].append(ultimo_segmento)

        # Subimos nivel
        level += 1

        #Iniciamos poma
        generate_piece()

    # Movemos la serpiente
    for i in reversed(range(len(snake["queue"]))):
        if i != 0:
            cercle_anterior = snake['queue'][i - 1]
            snake["queue"][i] = cercle_anterior
        else:
            snake["queue"][i] = get_next_snake_pos(delta_time)

def get_next_snake_pos(delta_time):
    # Calcula la següent posició de la serp basant-se en la posició del ratolí i l'estat de la serp (seguint o orbitant el ratolí).
    # Determina l'angle de direcció en funció de la distància i el pendent respecte al ratolí.
    
    global snake
    # Calcula la diferència en les coordenades entre el cap de la serp i el ratolí
    delta_x = mouse_pos['x'] - snake["queue"][0]['x']
    delta_y = mouse_pos['y'] - snake["queue"][0]['y']
   
    # Calcula la distància entre el cap de la serp i la posició del ratolí
    distancia = math.hypot(delta_x, delta_y)

    # Determina l'estat de la serp segons la distància al ratolí
    if distancia < 5:
        snake["status"] = 'orbit_mouse'  # Estat per orbitar prop del ratolí
    if distancia > 50:
        snake["status"] = 'follow_mouse'  # Estat per seguir el ratolí

    # Si la serp està en estat d'òrbita, 
    # augmenta l'angle de direcció per fer-la girar
    if snake["status"] == 'orbit_mouse':
        snake["direction_angle"] += distancia * math.pi / 1000
    else:
        # Calcula el pendent per obtenir l'angle; 
        # si delta_x és 0, s'estableix a infinit per evitar divisió per zero
        if delta_x != 0:
            pendent = delta_y / delta_x
        else:
            pendent = float('inf')

        # Calcula l'angle de direcció de la serp per seguir el ratolí
        if delta_x == 0 and mouse_pos['y'] < snake["queue"][0]['y']:
            # Angle per anar amunt (270 graus)
            snake["direction_angle"] = (3 * math.pi) / 2
        elif delta_x == 0 and mouse_pos['y'] >= snake["queue"][0]['y']:
            # Angle per anar avall (90 graus)
            snake["direction_angle"] = math.pi / 2
        elif mouse_pos['x'] > snake["queue"][0]['x']:
            # Angle per anar cap a la dreta 
            snake["direction_angle"] = math.atan(pendent)
        else:
            # Angle per anar cap a l'esquerra (180 graus)
            snake["direction_angle"] = math.atan(pendent) + math.pi

    return {
        "x": snake["queue"][0]['x'] + snake["speed"] * delta_time * math.cos(snake["direction_angle"]), 
        "y": snake["queue"][0]['y'] + snake["speed"] * delta_time * math.sin(snake["direction_angle"])
    }

def draw_board():
    # Mostra el nivell, la longitud de la serp, i la velocitat actual a la pantalla.
    padding = 20
    for i in range(1,4):
        x = padding
        y = padding * i
        if i == 1:
            text = f'Level: {level}'
        elif i == 2:
            text = f'Length: {len(snake["queue"])}'
        elif i == 3:
            text = f'Speed: {snake["speed"]:.2f}'
        board_text = font_board.render(text, True, BLACK)
        pos_text = (x, y)
        screen.blit(board_text, pos_text)

def draw_snake():
    # Dibuixa la serp segment per segment, aplicant un efecte de lluminositat que varia segons la posició del segment dins la cua.
    
    length_snake = len(snake['queue'])
    for i in reversed(range(length_snake)):
        value = 255 * (i / length_snake)
        color = (value, value, value)
        center = (snake["queue"][i]['x'], snake["queue"][i]['y'])
        pygame.draw.circle(screen, color, center, snake['radius'])

def draw_piece():
    # Dibuixa la peça actual a la pantalla en color vermell, incloent-hi el seu valor al centre de la peça.
    center = (piece['x'], piece["y"])
    pygame.draw.circle(screen, RED, center, piece["radius"])
    pygame.draw.circle(screen, BLACK, center, piece["radius"], 1)

    piece_text = font_piece.render(str(piece["value"]), True, BLACK)
    piece_rect = piece_text.get_rect()
    piece_rect.centerx = piece["x"]
    piece_rect.centery = piece["y"]
    screen.blit(piece_text, piece_rect)

if __name__ == '__main__':
    main()