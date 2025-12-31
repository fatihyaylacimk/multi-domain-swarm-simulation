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



import matplotlib.pyplot as plt

def render_gui(self, agents=None, goal=None):
    agents = agents if agents else []

    plt.figure(figsize=(6, 6))
    plt.xlim(0, self.width)
    plt.ylim(0, self.height)
    plt.gca().set_aspect('equal')
    plt.grid(True)

    # Obstacles
    for (x, y) in self.obstacles:
        plt.scatter(x + 0.5, y + 0.5, c='black', s=200)

    # Goal
    if goal:
        plt.scatter(goal[0] + 0.5, goal[1] + 0.5, c='green', s=200, marker='*')

    # Agents
    for agent in agents:
        plt.scatter(agent.x + 0.5, agent.y + 0.5, c='blue', s=100)

    plt.gca().invert_yaxis()
    plt.show()



