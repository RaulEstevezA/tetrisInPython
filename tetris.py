import pygame
import sys

from settings import WIDTH, HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, DROP_TIME, CONTROLS, GRID_SIZE, MARGIN_LEFT, MARGIN_TOP, LEVEL_UP_SCORE
from board import Board
from pieces import Piece
from menu import show_menu, show_game_over, configure_controls

# Inicializar pygame
pygame.init()

# Crear ventana
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# Inicializar el tablero y piezas
board = Board()
piece = Piece()
next_piece = Piece()

# Diccionario para rastrear teclas mantenidas
key_hold_times = {}
KEY_REPEAT_DELAY = 500  # Milisegundos antes de repetir
KEY_REPEAT_RATE = 100  # Intervalo de repetición

# Estado del juego
game_state = "menu"

# Nivel y puntuación inicial
score = 0
level = 1

# Temporizador de caída
last_drop_time = pygame.time.get_ticks()

while True:
    screen.fill(BLACK)

    if game_state == "menu":
        show_menu(screen)

    elif game_state == "playing":
        board.draw(screen, score, level)  # ✅ Ahora `board.draw()` maneja nivel y puntuación
        piece.draw(screen)

        # Dibujar la siguiente pieza en el lateral derecho
        next_piece_x = MARGIN_LEFT + WIDTH + 150
        next_piece_y = MARGIN_TOP + 100
        for i, row in enumerate(next_piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, next_piece.color,
                                     (next_piece_x + j * GRID_SIZE,
                                      next_piece_y + i * GRID_SIZE,
                                      GRID_SIZE, GRID_SIZE))

        # Ajustar la velocidad de caída según el nivel
        drop_speed = max(50, DROP_TIME - (level - 1) * 50)
        current_time = pygame.time.get_ticks()

        # Lógica de caída automática
        if current_time - last_drop_time > drop_speed:
            if not piece.move(0, 1, board):  # Si la pieza no puede seguir bajando
                if board.add_piece_to_board(piece, level):  
                    game_state = "game_over"
                else:
                    # 🔹 Corregir la suma de puntuación
                    lines_cleared, points = board.clear_full_rows(level)
                    if points > 0:
                        score += points
                        print(f"[DEBUG] Puntuación actualizada: {score}")  # Depuración

                    # Subir de nivel si es necesario
                    if score >= level * LEVEL_UP_SCORE:
                        level += 1

                    # Nueva pieza
                    piece = next_piece
                    next_piece = Piece()

                    if not piece._is_valid_position(piece.x, piece.y, piece.shape, board):
                        game_state = "game_over"

            last_drop_time = current_time  # Reiniciar temporizador de caída

    elif game_state == "game_over":
        screen.fill(BLACK)
        font = pygame.font.Font(None, 48)

        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {score:08d}", True, (255, 255, 255))

        game_over_x = (WINDOW_WIDTH - game_over_text.get_width()) // 2
        game_over_y = WINDOW_HEIGHT // 3
        score_x = (WINDOW_WIDTH - score_text.get_width()) // 2
        score_y = game_over_y + 60

        screen.blit(game_over_text, (game_over_x, game_over_y))
        screen.blit(score_text, (score_x, score_y))

        pygame.display.flip()

        # Esperar hasta que el jugador presione ENTER o cierre la ventana
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Reiniciar el juego
                        board = Board()
                        piece = Piece()
                        next_piece = Piece()
                        last_drop_time = pygame.time.get_ticks()
                        score = 0
                        level = 1
                        game_state = "menu"
                        waiting = False

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_state == "menu" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_state = "playing"
            elif event.key == pygame.K_c:
                CONTROLS = configure_controls(screen)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Manejo del movimiento de la pieza en estado "playing"
        elif game_state == "playing":
            if event.type == pygame.KEYDOWN:
                key_hold_times[event.key] = pygame.time.get_ticks()  # Guardar tiempo de pulsación
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

            elif event.type == pygame.KEYUP:
                if event.key in key_hold_times:
                    del key_hold_times[event.key]  # Eliminar la tecla cuando se suelta

    # 🔹 Restaurar el control de teclas mantenidas
    current_time = pygame.time.get_ticks()
    for key, press_time in list(key_hold_times.items()):  
        if current_time - press_time > KEY_REPEAT_DELAY:  
            if (current_time - press_time) % KEY_REPEAT_RATE < pygame.time.Clock().get_time():
                if key == CONTROLS["left"]:
                    piece.move(-1, 0, board)
                elif key == CONTROLS["right"]:
                    piece.move(1, 0, board)
                elif key == CONTROLS["down"]:
                    piece.move(0, 1, board)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
