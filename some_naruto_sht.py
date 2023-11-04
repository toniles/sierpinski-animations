import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants
SIDE_LENGTH = 1
NUM_FRAMES = 120
FRAME_INTERVAL = 100  # in milliseconds

# Functions to draw Sierpinski triangle and inscribed circles
def draw_sierpinski_triangle(ax, level, vertices):
    if level == 0:
        ax.fill(*zip(*vertices), color='blue')
    else:
        midpoints = [(vertices[i] + vertices[(i + 1) % 3]) / 2 for i in range(3)]
        smaller_triangles = [
            [vertices[0], midpoints[0], midpoints[2]],
            [vertices[1], midpoints[1], midpoints[0]],
            [vertices[2], midpoints[2], midpoints[1]],
        ]
        for triangle in smaller_triangles:
            draw_sierpinski_triangle(ax, level - 1, triangle)

def draw_inscribed_circles(ax, vertices, side_length):
    radius = (np.sqrt(3) / 6) * side_length
    centers = [((2 * vertices[i] + vertices[(i + 1) % 3]) / 3) for i in range(3)]
    for center in centers:
        ax.add_artist(plt.Circle(center, radius, color='green', fill=False))

# Animation update function
def update(frame, ax, vertices):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-1, 2)
    ax.set_ylim(-0.5, np.sqrt(3) / 2 + 0.5)

    # Rotate the triangle
    angle = 2 * np.pi * (frame / NUM_FRAMES)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_vertices = np.dot(vertices - vertices[0], rotation_matrix) + vertices[0]

    # Move the side vertices towards the top vertex
    if frame < NUM_FRAMES / 2:
        movement_factor = 2 * frame / NUM_FRAMES
        rotated_vertices[1:] = rotated_vertices[0] + (rotated_vertices[1:] - rotated_vertices[0]) * (1 - movement_factor)

    # Draw the updated triangle and circles
    draw_sierpinski_triangle(ax, 5, rotated_vertices)
    draw_inscribed_circles(ax, rotated_vertices, SIDE_LENGTH)

# Set up the figure and axis
fig, ax = plt.subplots()

# Initial triangle vertices
initial_vertices = np.array([
    [0, 0],
    [SIDE_LENGTH, 0],
    [SIDE_LENGTH / 2, np.sqrt(3) * SIDE_LENGTH / 2]
])

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=NUM_FRAMES, fargs=(ax, initial_vertices),
    interval=FRAME_INTERVAL, blit=False, repeat=False
)

plt.show()
