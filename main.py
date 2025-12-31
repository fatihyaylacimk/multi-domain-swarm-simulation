import matplotlib
matplotlib.use("TkAgg")



import matplotlib.pyplot as plt
import numpy as np

# Grid size
WIDTH = 10
HEIGHT = 10

# Obstacles
obstacles = [(3,3), (3,4), (3,5), (6,6), (7,6)]

def draw_grid(obstacles):
    grid = np.zeros((HEIGHT, WIDTH))

    for (x, y) in obstacles:
        grid[y][x] = 1  # obstacle

    plt.figure(figsize=(6,6))
    plt.imshow(grid, cmap="gray_r")

    plt.xticks(range(WIDTH))
    plt.yticks(range(HEIGHT))
    plt.grid(True)

    plt.title("Grid Map Background")
    plt.show()

draw_grid(obstacles)
