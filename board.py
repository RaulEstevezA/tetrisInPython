# board.py

import pygame
from settings import WIDTH, HEIGHT, GRID_SIZE, GRAY, LIGHT_GRAY, MARGIN_LEFT, MARGIN_TOP, ROWS, COLUMNS


class Board:
    def __init__(self):
        self.columns = WIDTH // GRID_SIZE
        self.rows = HEIGHT // GRID_SIZE
        self.grid = [[0] * self.columns for _ in range(self.rows)]

    def draw(self, screen):
        """Dibuja las piezas fijas, la cuadrícula y los bordes del tablero"""

        # Dibujar las piezas fijas primero
        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.grid[y][x] != 0:  # Si hay una pieza fija
                    pygame.draw.rect(screen, self.grid[y][x],  
                                    (MARGIN_LEFT + x * GRID_SIZE, 
                                    MARGIN_TOP + y * GRID_SIZE, 
                                    GRID_SIZE, GRID_SIZE))

        # Luego, dibujar la cuadrícula encima de las piezas
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, GRAY, 
                            (MARGIN_LEFT + x, MARGIN_TOP), 
                            (MARGIN_LEFT + x, MARGIN_TOP + HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, GRAY, 
                            (MARGIN_LEFT, MARGIN_TOP + y), 
                            (MARGIN_LEFT + WIDTH, MARGIN_TOP + y))

        # 🔹 Redibujar los bordes en la parte superior para asegurarse de que se vean
        pygame.draw.rect(screen, LIGHT_GRAY, 
                        (MARGIN_LEFT - GRID_SIZE, MARGIN_TOP, 
                        GRID_SIZE, HEIGHT))  # Borde izquierdo
        pygame.draw.rect(screen, LIGHT_GRAY, 
                        (MARGIN_LEFT + WIDTH, MARGIN_TOP, GRID_SIZE, 
                        HEIGHT))  # Borde derecho
        pygame.draw.rect(screen, LIGHT_GRAY, 
                        (MARGIN_LEFT - GRID_SIZE, MARGIN_TOP + HEIGHT, WIDTH + 
                        GRID_SIZE * 2, GRID_SIZE))  # Borde inferior




    def add_piece_to_board(self, piece):
        """Fija la pieza en el tablero y verifica si la partida debe terminar"""
        print("[DEBUG] Se ha llamado a add_piece_to_board")  # 🔹 Mensaje de depuración

        for i, row in enumerate(piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    grid_x = piece.x + j
                    grid_y = piece.y + i
                    if grid_y >= 0:  # Evitar errores si la pieza está en la parte superior
                        self.grid[grid_y][grid_x] = piece.color  # Guardar color

        # 🔹 Verificar si hay piezas en la primera fila (Game Over)
        if any(self.grid[0][x] != 0 for x in range(COLUMNS)):
            print("[DEBUG] La fila superior está ocupada, Game Over debe activarse")
            return True  # ⬅️ Ahora sí devuelve `True` para indicar Game Over

        self.clear_full_rows()  # Eliminar filas completas tras colocar la pieza
        return False  # Indicar que el juego sigue





    def add_piece_to_board(self, piece):
        """Fija la pieza en el tablero con su color correspondiente"""
        for i, row in enumerate(piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    grid_x = piece.x + j
                    grid_y = piece.y + i
                    if grid_y >= 0:  # Evitar errores si la pieza está en la parte superior
                        self.grid[grid_y][grid_x] = piece.color  # Ahora almacena el color de la pieza

        self.clear_full_rows()  # Eliminar filas completas tras colocar la pieza


    def clear_full_rows(self):
        """Elimina las filas completas y desplaza las superiores hacia abajo"""
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]  # Filtrar filas incompletas
        filas_eliminadas = self.rows - len(new_grid)  # Contar filas eliminadas

        while len(new_grid) < self.rows:  # Agregar nuevas filas vacías en la parte superior
            new_grid.insert(0, [0] * self.columns)

        self.grid = new_grid  # Reemplazar la cuadrícula por la nueva
        if filas_eliminadas > 0:
            print(f"[LÍNEAS] Eliminadas {filas_eliminadas} filas")




