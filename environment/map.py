import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np










import matplotlib.pyplot as plt
import numpy as np
    def render_visual(self, agents=None, goal=None):
        agents = agents if agents else []

        grid = np.zeros((self.height, self.width))

        # obstacles
        for (x, y) in self.obstacles:
            grid[y][x] = -1

        # goal
        if goal:
            gx, gy = goal
            grid[gy][gx] = 2

        # agents
        for a in agents:
            grid[a.y][a.x] = 1

        plt.figure(figsize=(6, 6))
        plt.imshow(grid, cmap="viridis")
        plt.title("Multi-Domain Swarm Simulation")
        plt.grid(True)
        
plt.show(block=True)
plt.figure(figsize=(6, 6))
plt.imshow(grid, cmap="viridis")
plt.title("Multi-Domain Swarm Simulation")
plt.grid(True)
plt.show(block=True)

def render_visual(self, agents=None, goal=None):
    grid = np.zeros((self.height, self.width))

    # Obstacles
    for (x, y) in self.obstacles:
        grid[y][x] = 1

    # Goal
    if goal:
        gx, gy = goal
        grid[gy][gx] = 3

    # Agents
    if agents:
        for a in agents:
            grid[a.y][a.x] = 2

    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="viridis")
    plt.title("Multi-Domain Swarm Simulation")
    plt.grid(True)
    plt.show(block=True)


