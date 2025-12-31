import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

from environment.map import GridMap
from agents.agent import Agent
from algorithms.bfs import bfs

# =========================
# SIMULATION SETUP
# =========================

width, height = 10, 10
obstacles = [(2,2), (2,3), (2,4), (4,5), (5,5), (6,5)]
goal = (5, 5)

grid = GridMap(width, height, obstacles)

agents = [
    Agent("LAND 1", 0, 0),
    Agent("LAND 2", 0, 1),
    Agent("LAND 3", 1, 0),
]

paths = {}

print("=== SIMULATION START ===")

for agent in agents:
    path = bfs(grid, agent.position(), goal)

    if not path:
        print(f"{agent.name} -> NO PATH FOUND")
        paths[agent.name] = []
        continue

    paths[agent.name] = path
    agent.x, agent.y = path[-1]

    print(f"{agent.name} path: {path}")
    print(f"{agent.name} final: {path[-1]}")

print("=== SIMULATION END ===")

# =========================
# VISUALIZATION
# =========================

plt.figure(figsize=(6, 6))
plt.xlim(0, grid.width)
plt.ylim(0, grid.height)
plt.gca().set_aspect("equal")

# Grid lines
for x in range(grid.width + 1):
    plt.plot([x, x], [0, grid.height], color="lightgray", linewidth=0.5)
for y in range(grid.height + 1):
    plt.plot([0, grid.width], [y, y], color="lightgray", linewidth=0.5)

# Obstacles
for (ox, oy) in grid.obstacles:
    plt.fill_between([ox, ox + 1], oy, oy + 1, color="black")

# Goal
plt.fill_between([goal[0], goal[0] + 1], goal[1], goal[1] + 1, color="green")

# Agent paths
colors = ["red", "blue", "orange"]
for (agent, color) in zip(agents, colors):
    path = paths.get(agent.name, [])
    if not path:
        continue

    xs = [p[0] + 0.5 for p in path]
    ys = [p[1] + 0.5 for p in path]
    plt.plot(xs, ys, marker="o", color=color, label=agent.name)

plt.legend()
plt.title("Multi-Domain Swarm Simulation")
plt.show()

input("Press Enter to exit...")
