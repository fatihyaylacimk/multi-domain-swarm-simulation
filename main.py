import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt




import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np

WIDTH = 6
HEIGHT = 6

obstacles = [
    (3, 3),
    (3, 4),
    (3, 5),
]

path = [
    (0, 0), (0, 1), (0, 2), (0, 3),
    (0, 4), (0, 5), (1, 5), (2, 5),
    (3, 5), (4, 5), (5, 5)
]

def draw_grid(obstacles, path):
    grid = np.zeros((HEIGHT, WIDTH))

    for (x, y) in obstacles:
        grid[y][x] = -1

    for (x, y) in path:
        grid[y][x] = 1

    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="gray_r", origin="lower")
    plt.grid(True)
    plt.title("Final Map View")

    # 🔴 EN KRİTİK SATIR
    plt.show(block=True)

draw_grid(obstacles, path)

# 🔴 POWERSHELL KAPANMASIN DİYE
input("Press Enter to exit...")
