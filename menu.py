# menu.py


import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, CONTROLS


# def show menu
def show_menu(screen):
    """Muestra el menú principal centrado en la pantalla"""
    screen.fill((0, 0, 0))  # Fondo negro
    font = pygame.font.Font(None, 48)

    # Mensajes del menú
    title = font.render("TETRIS", True, WHITE)
    start_text = font.render("Presiona ENTER para jugar", True, WHITE)
    controls_text = font.render("Presiona C para configurar controles", True, WHITE)
    exit_text = font.render("Presiona ESC para salir", True, WHITE)


    # Calcular posiciones centradas
    title_x = (WINDOW_WIDTH - title.get_width()) // 2
    title_y = (WINDOW_HEIGHT // 4)

    start_x = (WINDOW_WIDTH - start_text.get_width()) // 2
    start_y = (WINDOW_HEIGHT // 2)

    controls_x = (WINDOW_WIDTH - controls_text.get_width()) // 2
    controls_y = start_y + 50  

    exit_x = (WINDOW_WIDTH - exit_text.get_width()) // 2
    exit_y = controls_y + 50 


    # Dibujar textos centrados
    screen.blit(title, (title_x, title_y))
    screen.blit(start_text, (start_x, start_y))
    screen.blit(controls_text, (controls_x, controls_y))
    screen.blit(exit_text, (exit_x, exit_y))

    pygame.display.flip()


# def show menu pause
def show_pause_menu(screen):
    """Muestra el menú de pausa"""
    font = pygame.font.Font(None, 36)
    pause_text = font.render("Pausa - Presiona ENTER para continuar", True, (255, 255, 255))
    screen.blit(pause_text, (50, 300))
    pygame.display.flip()


# def menu game over
def show_game_over(screen):
    """Muestra la pantalla de Game Over centrada"""
    screen.fill((0, 0, 0))  # Fondo negro
    font = pygame.font.Font(None, 72)  # Tamaño más grande
    sub_font = pygame.font.Font(None, 36)  # Texto secundario más pequeño

    # Renderizar los textos
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    restart_text = sub_font.render("Presiona ENTER para volver al menú", True, (255, 255, 255))

    # Calcular posiciones centradas
    game_over_x = (WINDOW_WIDTH - game_over_text.get_width()) // 2
    game_over_y = (WINDOW_HEIGHT // 3)

    restart_x = (WINDOW_WIDTH - restart_text.get_width()) // 2
    restart_y = game_over_y + 100  # Un poco debajo del título

    # Dibujar textos centrados en la pantalla
    screen.blit(game_over_text, (game_over_x, game_over_y))
    screen.blit(restart_text, (restart_x, restart_y))

    pygame.display.flip()



# def menu configurar botones
def configure_controls(screen):
    """Permite al usuario cambiar las teclas de movimiento y devuelve el diccionario actualizado"""
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)

    text = font.render("Presiona la nueva tecla para cada acción", True, WHITE)
    screen.blit(text, ((WINDOW_WIDTH - text.get_width()) // 2, 50))

    actions = ["left", "right", "down", "drop", "rotate"]
    descriptions = ["Mover Izquierda", "Mover Derecha", "Bajar", "Caída Rápida", "Rotar"]
    
    new_controls = {}

    for i, action in enumerate(actions):
        prompt = font.render(f"{descriptions[i]}: Presiona una tecla", True, WHITE)
        screen.blit(prompt, (50, 150 + i * 50))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    new_controls[action] = event.key
                    waiting = False

    return new_controls  # En lugar de modificar `CONTROLS` directamente

