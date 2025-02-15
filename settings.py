# settings.py

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

# Lista de colores para las piezas
COLORS = [
    (255, 0, 0),   # Rojo
    (0, 255, 0),   # Verde
    (0, 0, 255),   # Azul
    (255, 255, 0), # Amarillo
    (255, 165, 0), # Naranja
    (128, 0, 128)  # Púrpura
]
