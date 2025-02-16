# pieces.py

import pygame
import random
from settings import GRID_SIZE, COLUMNS, ROWS, COLORS, MARGIN_LEFT, MARGIN_TOP

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
        """Inicializa una nueva pieza de Tetris en el centro del tablero"""
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2  # Centrar en columnas
        self.y = -len(self.shape)  # Para que aparezca justo fuera del tablero

    def draw(self, screen):
        """Dibuja la pieza en la pantalla con los márgenes aplicados"""
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color, 
                                     (MARGIN_LEFT + (self.x + j) * GRID_SIZE, 
                                      MARGIN_TOP + (self.y + i) * GRID_SIZE, 
                                      GRID_SIZE, GRID_SIZE))
    
    def rotate(self):
        """Rota la pieza en sentido horario 90° si es válido"""
        rotated_shape = list(zip(*self.shape[::-1]))  # Gira la matriz temporalmente
        rotated_shape = [list(row) for row in rotated_shape]  # Convertir a lista de listas
        
        # Ajustar la posición si la rotación se sale del tablero
        min_x = min(j for i, row in enumerate(rotated_shape) for j, cell in enumerate(row) if cell)
        max_x = max(j for i, row in enumerate(rotated_shape) for j, cell in enumerate(row) if cell)
        
        if self.x + min_x < 0:
            self.x -= (self.x + min_x)  # Ajusta si se sale por la izquierda
        elif self.x + max_x >= COLUMNS:
            self.x -= (self.x + max_x - COLUMNS + 1)  # Ajusta si se sale por la derecha
        
        if self._is_valid_position(self.x, self.y, rotated_shape):
            self.shape = rotated_shape  # Solo aplicar si es una rotación válida
    
    def move(self, dx, dy):
        """Mueve la pieza en el tablero si es un movimiento válido"""
        if self._is_valid_position(self.x + dx, self.y + dy, self.shape):
            self.x += dx
            self.y += dy
    
    def _is_valid_position(self, new_x, new_y, shape):
        """Verifica si la nueva posición está dentro del tablero"""
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    if new_x + j < 0 or new_x + j >= COLUMNS:
                        return False  # Se salió por izquierda o derecha
                    if new_y + i >= ROWS:
                        return False  # Se salió por abajo
        return True

