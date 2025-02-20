import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, CONTROLS


def show_menu(screen):
    """muestra el menu principal centrado en la pantalla"""
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 48)

    title = font.render("TETRIS", True, WHITE)
    start_text = font.render("presiona ENTER para jugar", True, WHITE)
    controls_text = font.render("presiona C para configurar controles", True, WHITE)
    exit_text = font.render("presiona ESC para salir", True, WHITE)

    title_x = (WINDOW_WIDTH - title.get_width()) // 2
    title_y = (WINDOW_HEIGHT // 4)

    start_x = (WINDOW_WIDTH - start_text.get_width()) // 2
    start_y = (WINDOW_HEIGHT // 2)

    controls_x = (WINDOW_WIDTH - controls_text.get_width()) // 2
    controls_y = start_y + 50

    exit_x = (WINDOW_WIDTH - exit_text.get_width()) // 2
    exit_y = controls_y + 50

    screen.blit(title, (title_x, title_y))
    screen.blit(start_text, (start_x, start_y))
    screen.blit(controls_text, (controls_x, controls_y))
    screen.blit(exit_text, (exit_x, exit_y))

    pygame.display.flip()


def show_pause_menu(screen):
    """muestra el menu de pausa"""
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 48)
    pause_text = font.render("PAUSA", True, (255, 255, 0))
    resume_text = font.render("presiona ESC para continuar", True, (255, 255, 255))

    pause_x = (WINDOW_WIDTH - pause_text.get_width()) // 2
    pause_y = (WINDOW_HEIGHT // 3)

    resume_x = (WINDOW_WIDTH - resume_text.get_width()) // 2
    resume_y = pause_y + 100

    screen.blit(pause_text, (pause_x, pause_y))
    screen.blit(resume_text, (resume_x, resume_y))

    pygame.display.flip()


def show_game_over(screen):
    """muestra la pantalla de game over centrada"""
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 72)
    sub_font = pygame.font.Font(None, 36)

    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    restart_text = sub_font.render("presiona ENTER para volver al menu", True, (255, 255, 255))

    game_over_x = (WINDOW_WIDTH - game_over_text.get_width()) // 2
    game_over_y = (WINDOW_HEIGHT // 3)

    restart_x = (WINDOW_WIDTH - restart_text.get_width()) // 2
    restart_y = game_over_y + 100

    screen.blit(game_over_text, (game_over_x, game_over_y))
    screen.blit(restart_text, (restart_x, restart_y))

    pygame.display.flip()


def configure_controls(screen):
    """permite al usuario cambiar las teclas de movimiento y devuelve el diccionario actualizado"""
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)

    text = font.render("presiona la nueva tecla para cada accion", True, WHITE)
    screen.blit(text, ((WINDOW_WIDTH - text.get_width()) // 2, 50))

    actions = ["left", "right", "down", "drop", "rotate"]
    descriptions = ["mover izquierda", "mover derecha", "bajar", "caida rapida", "rotar"]

    new_controls = {}

    for i, action in enumerate(actions):
        prompt = font.render(f"{descriptions[i]}: presiona una tecla", True, WHITE)
        screen.blit(prompt, (50, 150 + i * 50))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key != pygame.K_ESCAPE:  # prevenir ESC como tecla configurable
                        new_controls[action] = event.key
                        waiting = False

    return new_controls
