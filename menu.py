import pygame

def show_menu(screen):
    """Muestra el menú principal"""
    screen.fill((0, 0, 0))  # Fondo negro
    font = pygame.font.Font(None, 48)
    title = font.render("TETRIS", True, (255, 255, 255))
    start_text = font.render("Presiona ENTER para jugar", True, (255, 255, 255))
    exit_text = font.render("Presiona ESC para salir", True, (255, 255, 255))
    
    screen.blit(title, (100, 150))
    screen.blit(start_text, (50, 300))
    screen.blit(exit_text, (50, 350))
    pygame.display.flip()

def show_pause_menu(screen):
    """Muestra el menú de pausa"""
    font = pygame.font.Font(None, 36)
    pause_text = font.render("Pausa - Presiona ENTER para continuar", True, (255, 255, 255))
    screen.blit(pause_text, (50, 300))
    pygame.display.flip()

def show_game_over(screen):
    """Muestra la pantalla de Game Over"""
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 48)
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    restart_text = font.render("Presiona ENTER para reiniciar", True, (255, 255, 255))
    screen.blit(game_over_text, (80, 250))
    screen.blit(restart_text, (50, 350))
    pygame.display.flip()