import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np

N, F, lvl, frames, interval = 5, 30, 5, 30, 200

def s(nivel):
    t = [np.array([[-0.5, 0], [0.5, 0], [0, np.sqrt(3)/2]])]
    for _ in range(nivel):
        r = []
        for tri in t:
            A, B, C = (tri[0] + tri[1]) / 2, (tri[1] + tri[2]) / 2, (tri[0] + tri[2]) / 2
            r += [np.array([tri[0], A, C]), np.array([A, tri[1], B]), np.array([C, B, tri[2]])]
        t = r
    return t

def a(t, i, m):
    f = i / m
    return [np.array([np.array([p[0] * (1 + f * abs(p[0])) if p[1] else p[0], p[1] * (1 + f) if p[1] else p[1]]) for p in tri]) for tri in t]

fig, ax = plt.subplots()
ax.set(aspect='equal', xlim=(-1, 1), ylim=(-0.1, 1))
ax.axis('off')
p = PatchCollection([], facecolor='white', edgecolor='black', linewidths=0.5)
ax.add_collection(p)

def init():
    p.set_paths([])
    return [p]

def animate(i):
    global t
    t = s(N) if i == 0 else a(t, i, F)
    p.set_paths([Polygon(tri, closed=True) for tri in t])
    return [p]

anim = FuncAnimation(fig, animate, init_func=init, frames=frames + 1, interval=interval, blit=False)
plt.show()
