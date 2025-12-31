# =========================
# Multi-Domain Swarm Simulation
# main.py
# =========================

from environment.map import GridMap
from agents.agent import Agent
from algorithms.prioritized_astar import prioritized_astar

# -------------------------
# SIMULATION SETUP
# -------------------------
print("=== SIMULATION START ===")

# Grid map
width = 10
height = 10
obstacles = []  # obstacle eklemek istersen [(x,y), ...]
grid = GridMap(width, height, obstacles)

# Goal
goal = (5, 5)

# Agents
agents = [
    Agent("LAND 1", 0, 0, speed=1),
    Agent("LAND 2", 1, 0, speed=1),
    Agent("LAND 3", 2, 0, speed=1),
]

# -------------------------
# PATH PLANNING
# -------------------------
paths = prioritized_astar(grid, agents, goal)

# -------------------------
# RESULTS
# -------------------------
for name, path in paths.items():
    if len(path) == 0:
        print(f"{name} path: []")
        print(f"{name} final: NO MOVE")
    else:
        print(f"{name} path: {path}")
        print(f"{name} final: {path[-1]}")

# -------------------------
# FINAL MAP (GUI)
# -------------------------
print("\nFINAL MAP VIEW:")
grid.render_gui(agents, goal)

print("=== SIMULATION END ===")
