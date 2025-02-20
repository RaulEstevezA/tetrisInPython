import pygame
import sys

from settings import (
    WIDTH, HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, DROP_TIME,
    CONTROLS, GRID_SIZE, MARGIN_LEFT, MARGIN_TOP, LEVEL_UP_SCORE,
    LINE_CLEAR_COEFFICIENTS, LEVEL_COEFFICIENTS, calculate_drop_speed,
    KEY_REPEAT_DELAY, KEY_REPEAT_RATE
)
from board import Board
from pieces import Piece
from menu import show_menu, show_game_over, configure_controls, show_pause_menu

# inicializar pygame
pygame.init()
pygame.mixer.init()

# cargar y reproducir musica de fondo
pygame.mixer.music.load('music/tetrisBase.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

# crear ventana
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# inicializar el tablero y piezas
board = Board()
piece = Piece()
next_piece = Piece()

# diccionario para rastrear teclas mantenidas
key_hold_times = {}

# estado del juego
game_state = "menu"

# nivel y puntuacion inicial
score = 0
level = 1

# temporizador de caida
last_drop_time = pygame.time.get_ticks()
clock = pygame.time.Clock()

while True:
    screen.fill(BLACK)

    if game_state == "menu":
        show_menu(screen)

    elif game_state == "playing":
        board.draw(screen, score, level)
        piece.draw(screen)

        # dibujar la siguiente pieza
        next_piece_x = MARGIN_LEFT + WIDTH + 150
        next_piece_y = MARGIN_TOP + 100
        for i, row in enumerate(next_piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, next_piece.color,
                                     (next_piece_x + j * GRID_SIZE,
                                      next_piece_y + i * GRID_SIZE,
                                      GRID_SIZE, GRID_SIZE))

        # calcular velocidad de caida
        drop_speed = calculate_drop_speed(level)
        current_time = pygame.time.get_ticks()

        # logica de caida automatica
        if current_time - last_drop_time > drop_speed:
            if not piece.move(0, 1, board):
                if board.add_piece_to_board(piece, level):
                    game_state = "game_over"
                else:
                    # puntuacion
                    lines_cleared, _ = board.clear_full_rows(level)
                    if lines_cleared > 0:
                        line_coefficient = LINE_CLEAR_COEFFICIENTS.get(lines_cleared, 1)
                        level_coefficient = LEVEL_COEFFICIENTS.get(level, 1)
                        points = int((10 * lines_cleared) * line_coefficient * level_coefficient)
                        score += points

                    # subir de nivel
                    if score >= level * LEVEL_UP_SCORE:
                        level += 1

                    # nueva pieza
                    piece = next_piece
                    next_piece = Piece()

                    # verificar espacio
                    if not piece._is_valid_position(piece.x, piece.y, piece.shape, board):
                        game_state = "game_over"

            last_drop_time = current_time

    elif game_state == "paused":
        show_pause_menu(screen)

    elif game_state == "game_over":
        pygame.mixer.music.stop()
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

        # esperar entrada
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.play(-1)
                        board = Board()
                        piece = Piece()
                        next_piece = Piece()
                        last_drop_time = pygame.time.get_ticks()
                        score = 0
                        level = 1
                        game_state = "menu"
                        waiting = False

    # eventos
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

        elif game_state == "playing":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = "paused"
                else:
                    key_hold_times[event.key] = pygame.time.get_ticks()
                    if event.key == CONTROLS["left"]:
                        piece.move(-1, 0, board)
                    elif event.key == CONTROLS["right"]:
                        piece.move(1, 0, board)
                    elif event.key == CONTROLS["down"]:
                        piece.move(0, 1, board)
                    elif event.key == CONTROLS["drop"]:
                        # hacer que la pieza caiga hasta el fondo instantaneamente
                        while piece.move(0, 1, board):
                            pass
                        board.add_piece_to_board(piece, level)
                    elif event.key == CONTROLS["rotate"]:
                        piece.rotate(board)

            elif event.type == pygame.KEYUP:
                if event.key in key_hold_times:
                    del key_hold_times[event.key]

        elif game_state == "paused" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = "playing"

    # teclas mantenidas con control de retardo y repeticion
    current_time = pygame.time.get_ticks()
    for key in list(key_hold_times.keys()):
        if current_time - key_hold_times[key] >= KEY_REPEAT_DELAY:
            if key == CONTROLS["left"]:
                piece.move(-1, 0, board)
                key_hold_times[key] = current_time - (KEY_REPEAT_DELAY - KEY_REPEAT_RATE)
            elif key == CONTROLS["right"]:
                piece.move(1, 0, board)
                key_hold_times[key] = current_time - (KEY_REPEAT_DELAY - KEY_REPEAT_RATE)
            elif key == CONTROLS["down"]:
                piece.move(0, 1, board)
                key_hold_times[key] = current_time - (KEY_REPEAT_DELAY - KEY_REPEAT_RATE)

    pygame.display.flip()
    clock.tick(60)
