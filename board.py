# board.py

import pygame
from settings import WIDTH, HEIGHT, GRID_SIZE, GRAY, LIGHT_GRAY, MARGIN_LEFT, MARGIN_TOP

class Board:
    def __init__(self):
        self.columns = WIDTH // GRID_SIZE
        self.rows = HEIGHT // GRID_SIZE
        self.grid = [[0] * self.columns for _ in range(self.rows)]

    def draw(self, screen):
        """Dibuja la cuadrícula en la pantalla, centrada con los márgenes"""
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, GRAY, 
                             (MARGIN_LEFT + x, MARGIN_TOP), 
                             (MARGIN_LEFT + x, MARGIN_TOP + HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, GRAY, 
                             (MARGIN_LEFT, MARGIN_TOP + y), 
                             (MARGIN_LEFT + WIDTH, MARGIN_TOP + y))

                # 🔹 Dibujar bordes alrededor del tablero con gris más claro
        pygame.draw.rect(screen, LIGHT_GRAY, 
                         (MARGIN_LEFT - GRID_SIZE, MARGIN_TOP, 
                          GRID_SIZE, HEIGHT))  # Borde izquierdo
        pygame.draw.rect(screen, LIGHT_GRAY, 
                         (MARGIN_LEFT + WIDTH, MARGIN_TOP, GRID_SIZE, 
                          HEIGHT))  # Borde derecho
        pygame.draw.rect(screen, LIGHT_GRAY, 
                         (MARGIN_LEFT - GRID_SIZE, MARGIN_TOP + HEIGHT, WIDTH + 
                          GRID_SIZE * 2, GRID_SIZE))  # Borde inferior



