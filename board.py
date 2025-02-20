import pygame
from settings import WIDTH, HEIGHT, GRID_SIZE, GRAY, LIGHT_GRAY, MARGIN_LEFT, MARGIN_TOP, ROWS, COLUMNS, WINDOW_HEIGHT

class Board:
    def __init__(self):
        self.columns = WIDTH // GRID_SIZE
        self.rows = HEIGHT // GRID_SIZE
        self.grid = [[0] * self.columns for _ in range(self.rows)]

    def draw(self, screen, score, level):
        """dibuja las piezas fijas, la cuadrícula, el nivel y la puntuación"""
        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.grid[y][x] != 0:
                    pygame.draw.rect(screen, self.grid[y][x],  
                                    (MARGIN_LEFT + x * GRID_SIZE, 
                                    MARGIN_TOP + y * GRID_SIZE, 
                                    GRID_SIZE, GRID_SIZE))

        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, GRAY, 
                            (MARGIN_LEFT + x, MARGIN_TOP), 
                            (MARGIN_LEFT + x, MARGIN_TOP + HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, GRAY, 
                            (MARGIN_LEFT, MARGIN_TOP + y), 
                            (MARGIN_LEFT + WIDTH, MARGIN_TOP + y))

        pygame.draw.rect(screen, LIGHT_GRAY, (MARGIN_LEFT - GRID_SIZE, 
                                              MARGIN_TOP, GRID_SIZE, HEIGHT))
        pygame.draw.rect(screen, LIGHT_GRAY, (MARGIN_LEFT + WIDTH, 
                                              MARGIN_TOP, GRID_SIZE, HEIGHT))
        pygame.draw.rect(screen, LIGHT_GRAY, (MARGIN_LEFT - GRID_SIZE, 
                                              MARGIN_TOP + HEIGHT, WIDTH + 
                                              GRID_SIZE * 2, GRID_SIZE))

        self.draw_level(screen, level)
        self.draw_score(screen, score)

    def draw_level(self, screen, level):
        """dibuja el nivel en la parte superior izquierda"""
        font = pygame.font.Font(None, 36)
        level_text = font.render(f"Level: {level}", True, (255, 255, 255))
        level_x = MARGIN_LEFT // 2 - level_text.get_width() // 2
        level_y = 100
        screen.blit(level_text, (level_x, level_y))

    def draw_score(self, screen, score):
        """dibuja la puntuación en la parte inferior izquierda con 8 cifras"""
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score:08d}", True, (255, 255, 255))
        score_x = MARGIN_LEFT // 2 - score_text.get_width() // 2
        score_y = WINDOW_HEIGHT - 100
        screen.blit(score_text, (score_x, score_y))

    def add_piece_to_board(self, piece, level):
        """fija la pieza en el tablero y verifica si la partida debe terminar"""
        for i, row in enumerate(piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    grid_x = piece.x + j
                    grid_y = piece.y + i
                    if grid_y >= 0:
                        self.grid[grid_y][grid_x] = piece.color

        for x in range(self.columns):
            if self.grid[0][x] != 0:
                return True
        return False

    def clear_full_rows(self, level):
        """elimina las filas completas y calcula la puntuación basada en el nivel"""
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        lines_cleared = self.rows - len(new_grid)

        points_earned = 0
        if lines_cleared > 0:
            points_earned = (10 + 10 * (lines_cleared - 1)) * level

        while len(new_grid) < self.rows:
            new_grid.insert(0, [0] * self.columns)

        self.grid = new_grid
        return lines_cleared, points_earned
