import pygame
import sys


from settings import WIDTH, HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, DROP_TIME, CONTROLS
from board import Board
from pieces import Piece
from menu import show_menu, show_pause_menu, show_game_over, configure_controls


# Inicializar pygame
pygame.init()


# Crear ventana
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")


# Inicializar el tablero
board = Board()
piece = Piece()


# Bucle principal
game_state = "menu"
running = True
clock = pygame.time.Clock()
last_drop_time = pygame.time.get_ticks()  # Guarda el tiempo inicial


while running:
    screen.fill(BLACK)
    
    if game_state == "menu":
        show_menu(screen)
    elif game_state == "playing":
        board.draw(screen)
        piece.draw(screen)

        # Lógica de gravedad: hacer que la pieza caiga automáticamente
        current_time = pygame.time.get_ticks()
        if current_time - last_drop_time > DROP_TIME:
            piece.y += 1  # La pieza baja una celda
            last_drop_time = current_time  # Reiniciar el temporizador
    
    elif game_state == "game_over":
        show_game_over(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter para empezar el juego
                game_state = "playing"
            elif event.key == pygame.K_c:  # C para configurar controles
                configure_controls(screen)
            elif event.key == pygame.K_ESCAPE:  # ESC para salir
                running = False
        
        # Manejo del movimiento de la pieza en estado "playing"
        elif game_state == "playing" and event.type == pygame.KEYDOWN:
            if event.key == CONTROLS["left"]:  # Mover izquierda
                piece.x -= 1
            elif event.key == CONTROLS["right"]:  # Mover derecha
                piece.x += 1
            elif event.key == CONTROLS["down"]:  # Mover abajo
                piece.y += 1
            elif event.key == CONTROLS["drop"]:  # Caída rápida
                piece.y += 5  # Baja varias filas instantáneamente
            elif event.key == CONTROLS["rotate"]:  # Rotar la pieza
                # Llamaremos a una función de rotación (aún por definir en pieces.py)
                piece.rotate()

    pygame.display.flip()
    clock.tick(10)


pygame.quit()
sys.exit()
