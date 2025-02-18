# tetris.py 




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
            if not piece.move(0, 1, board):  # Si la pieza no puede seguir bajando
                if board.add_piece_to_board(piece):  # Fijarla y comprobar si se debe terminar el juego
                    print("[GAME OVER] La partida ha terminado")
                    game_state = "game_over"
                else:
                    # Generar una nueva pieza
                    new_piece = Piece()
                    if not new_piece._is_valid_position(new_piece.x, new_piece.y, new_piece.shape, board):
                        print("[GAME OVER] No hay espacio para la nueva pieza")
                        game_state = "game_over"
                    else:
                        piece = new_piece  # Asignar la nueva pieza correctamente





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
                CONTROLS = configure_controls(screen)  # ⬅️ Ahora guardamos los nuevos controles
            elif event.key == pygame.K_ESCAPE:  # ESC para salir
                running = False

        
        # Manejo del movimiento de la pieza en estado "playing"
        elif game_state == "playing" and event.type == pygame.KEYDOWN:
            if event.key == CONTROLS["left"]:
                piece.move(-1, 0, board)
            elif event.key == CONTROLS["right"]:
                piece.move(1, 0, board)
            elif event.key == CONTROLS["down"]:
                piece.move(0, 1, board)
            elif event.key == CONTROLS["drop"]:
                piece.move(0, 5, board)
            elif event.key == CONTROLS["rotate"]:
                piece.rotate(board)


    pygame.display.flip()
    clock.tick(10)


pygame.quit()
sys.exit()

