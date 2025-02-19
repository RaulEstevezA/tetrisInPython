# settings.py


import pygame

# Tamaño de la pantalla
WIDTH = 300
HEIGHT = 600

# Márgenes para centrar el tablero
MARGIN_LEFT = 500  # Espacio a la izquierda
MARGIN_TOP = 100    # Espacio arriba


# Espacio adicional en la ventana
WINDOW_WIDTH = MARGIN_LEFT + WIDTH + 500 
WINDOW_HEIGHT = MARGIN_TOP + HEIGHT + 100  

# Tamaño de cada celda en la cuadrícula
GRID_SIZE = 30  

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LIGHT_GRAY = (180, 180, 180)


# Columnas del Tetris
COLUMNS = 10 
# Número de filas en el tablero de Tetris
ROWS = 20  # Altura estándar del tablero 

# Lista de colores para las piezas
COLORS = [
    (255, 0, 0),   # Rojo
    (0, 255, 0),   # Verde
    (0, 0, 255),   # Azul
    (255, 255, 0), # Amarillo
    (255, 165, 0), # Naranja
    (128, 0, 128)  # Púrpura
]


# Controles por defecto
DEFAULT_CONTROLS = {
    "left": pygame.K_LEFT,      # Flecha izquierda
    "right": pygame.K_RIGHT,    # Flecha derecha
    "down": pygame.K_DOWN,      # Flecha abajo
    "drop": pygame.K_SPACE,     # Barra espaciadora
    "rotate": pygame.K_UP       # Flecha arriba
}

# Controles personalizables (inicialmente iguales a los predeterminados)
CONTROLS = DEFAULT_CONTROLS.copy()


# Velocidad de caída de las piezas (milisegundos)
DROP_TIME = 500  # Cada 500ms la pieza bajará una celda


# Puntuación necesaria para subir de nivel
LEVEL_UP_SCORE = 1000  # Cambiar este valor si quieres que el nivel suba más rápido o más lento