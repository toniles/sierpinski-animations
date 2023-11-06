import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np

# Variables hardcodeadas
NIVEL = 6
FRAMES = 144
INTERVALO = 100

def generar_colores_pastel(num_colores):
    return np.random.rand(num_colores, 3) * 0.6 + 0.4

def generar_sierpinski(nivel):
    triangulos = [np.array([[-0.5, 0], [0.5, 0], [0, np.sqrt(3)/2]])]
    colores = generar_colores_pastel(1)
    for i in range(nivel):
        nuevos_triangulos = []
        nuevos_colores = generar_colores_pastel(len(triangulos) * 3)
        for j, tri in enumerate(triangulos):
            A = (tri[0] + tri[1]) / 2
            B = (tri[1] + tri[2]) / 2
            C = (tri[0] + tri[2]) / 2
            nuevos_triangulos += [np.array([tri[0], A, C]), np.array([A, tri[1], B]), np.array([C, B, tri[2]])]
        triangulos = nuevos_triangulos
        colores = nuevos_colores
    return triangulos, colores

def subdividir_triangulos(triangulos):
    resultado = []
    for tri in triangulos:
        A = (tri[0] + tri[1]) / 2
        B = (tri[1] + tri[2]) / 2
        C = (tri[0] + tri[2]) / 2
        resultado += [np.array([tri[0], A, C]), np.array([A, tri[1], B]), np.array([C, B, tri[2]])]
    return resultado

def abrir_fractal(triangulos, iteracion, max_iteraciones, altura_base):
    apertura = (iteracion / max_iteraciones) * np.pi / 2
    def mover_punto(punto):
        if punto[1] <= altura_base:
            return punto
        altura = punto[1] - altura_base
        factor = altura / (np.sqrt(3)/2)
        angulo = apertura * factor
        rotacion = np.array([[np.cos(angulo), -np.sin(angulo)], [np.sin(angulo), np.cos(angulo)]])
        nuevo_punto = np.dot(rotacion, punto - np.array([0, altura_base])) + np.array([0, altura_base])
        return nuevo_punto
    nuevos_triangulos = []
    for tri in triangulos:
        nuevos_triangulos.append(np.array([mover_punto(punto) for punto in tri]))
    return nuevos_triangulos

def init():
    patch.set_paths([])
    return [patch]

def animate(i):
    global triangulos, colores
    if i == 0:
        triangulos, colores = generar_sierpinski(NIVEL)
    else:
        triangulos = abrir_fractal(triangulos, iteracion=i, max_iteraciones=FRAMES, altura_base=0)
    patches_data = [Polygon(tri, closed=True) for tri in triangulos]
    patch.set_color(colores)
    patch.set_paths(patches_data)
    return [patch]

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-1, 1)
ax.set_ylim(-0.1, 1)
triangulos, colores = generar_sierpinski(NIVEL)
patch = PatchCollection([Polygon(tri, closed=True) for tri in triangulos], facecolor=colores, edgecolor='black', linewidths=0.5)
ax.add_collection(patch)

anim = FuncAnimation(fig, animate, init_func=init, frames=FRAMES + 1, interval=INTERVALO, blit=False)

#lo guardamos como gif
anim.save('sierpinski.gif', writer='imagemagick')
#plt.show()
