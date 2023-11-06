import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Polygon

# Variables configurables
MAX_ORDER = 5  # Número máximo de niveles del triángulo de Sierpinski a dibujar
INTERVAL = 100  # Intervalo en milisegundos entre cuadros
PLEGAR_FRAMES = 60  # Número de cuadros para realizar el "plegado"

# Función para calcular la rotación de un punto alrededor de otro punto dado un ángulo
def rotate(point, origin, angle):
    ox, oy = origin
    px, py = point

    qx = ox + np.cos(angle) * (px - ox) - np.sin(angle) * (py - oy)
    qy = oy + np.sin(angle) * (px - ox) + np.cos(angle) * (py - oy)
    return qx, qy

# Función para dibujar el triángulo de Sierpinski que se pliega en un árbol fractal
def plot_sierpinski_fold(vertices, order, angle, ax):
    if order == 0:
        # Dibuja el triángulo base
        triangle = Polygon(vertices, closed=True, color='b')
        ax.add_patch(triangle)
    else:
        # Calcula los puntos medios y rotaciones
        midpoints = [(vertices[i] + vertices[(i + 1) % 3]) / 2.0 for i in range(3)]
        # Puntos después de la rotación
        rotated_midpoints = [
            rotate(midpoints[i], vertices[i], angle) for i in range(3)
        ]

        # Forma los nuevos triángulos para la siguiente iteración
        sierpinski_triangles = [
            [vertices[0], rotated_midpoints[0], rotated_midpoints[2]],
            [vertices[1], rotated_midpoints[1], rotated_midpoints[0]],
            [vertices[2], rotated_midpoints[2], rotated_midpoints[1]],
        ]

        for triangle in sierpinski_triangles:
            plot_sierpinski_fold(np.array(triangle), order - 1, angle, ax)

# Actualizar la función para la animación
def update_fold(frame_number, vertices, MAX_ORDER, PLEGAR_FRAMES, ax):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-0.1, np.sqrt(3) + 0.1)

    # Calcular el ángulo actual basado en el número de cuadro
    if frame_number <= MAX_ORDER:
        angle = np.radians(120)  # Ángulo inicial de 120 grados
    else:
        # Reducir el ángulo gradualmente hasta 0
        angle = np.radians(120) * (1 - (frame_number - MAX_ORDER) / PLEGAR_FRAMES)

    # Dibujar el triángulo de Sierpinski que se pliega en un árbol fractal
    plot_sierpinski_fold(vertices, MAX_ORDER, angle, ax)

    return ax,

# Configuración inicial de la figura y los vértices iniciales
fig, ax = plt.subplots()
vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])

# Crear la animación
ani = animation.FuncAnimation(fig, update_fold, fargs=(vertices, MAX_ORDER, PLEGAR_FRAMES, ax),
                              frames=np.arange(0, MAX_ORDER + PLEGAR_FRAMES + 1),
                              interval=INTERVAL, blit=False, repeat=False)

plt.show()
