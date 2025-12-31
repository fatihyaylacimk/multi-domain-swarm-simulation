import matplotlib.pyplot as plt
import numpy as np

class GridMap:
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.obstacles = obstacles if obstacles else []

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_free(self, x, y):
        return (x, y) not in self.obstacles

    def neighbors(self, x, y):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        result = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny) and self.is_free(nx, ny):
                result.append((nx, ny))
        return result

    def render_visual(self, agents=None, goal=None):
        grid = np.zeros((self.height, self.width))

        for (x, y) in self.obstacles:
            grid[y][x] = -1

        if agents:
            for a in agents:
                grid[a.y][a.x] = 2

        if goal:
            gx, gy = goal
            grid[gy][gx] = 3

        plt.figure(figsize=(6,6))
        plt.imshow(grid, cmap="viridis")
        plt.grid(True)
        plt.xticks(range(self.width))
        plt.yticks(range(self.height))
        plt.title("Multi-Domain Swarm Simulation")
        plt.show()
