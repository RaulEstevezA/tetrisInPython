# pieces.py

import pygame
import random
from settings import GRID_SIZE, COLUMNS, COLORS

# Definición de las formas del Tetris
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

class Piece:
    def __init__(self):
        """Inicializa una nueva pieza de Tetris en una posición aleatoria."""
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def draw(self, screen):
        """Dibuja la pieza en la pantalla."""
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color, 
                                     ((self.x + j) * GRID_SIZE, 
                                      (self.y + i) * GRID_SIZE, 
                                      GRID_SIZE, GRID_SIZE))
