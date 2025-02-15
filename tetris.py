import pygame
import sys


from settings import WIDTH, HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from board import Board
from pieces import Piece
from menu import show_menu, show_pause_menu, show_game_over


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


while running:

    screen.fill(BLACK)
    
    if game_state == "menu":
        show_menu(screen)
    elif game_state == "playing":
        board.draw(screen)
        piece.draw(screen)
    elif game_state == "game_over":
        show_game_over(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_state == "menu" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter para empezar el juego
                game_state = "playing"
            elif event.key == pygame.K_ESCAPE:  # ESC para salir
                running = False
        
        elif game_state == "playing" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # ESC para pausar
                game_state = "menu"
    
    pygame.display.flip()
    clock.tick(10)


pygame.quit()
sys.exit()
