# =========================
# MAIN ENTRY POINT
# =========================

from cevre.map import GridMap
from agents.agent import Agent
from algorithms.prioritized_astar import prioritized_astar

print("=== SIMULATION START ===")

# -------------------------
# GRID SETUP
# -------------------------
width = 10
height = 10

obstacles = [
    (2, 2), (2, 3), (2, 4),
    (4, 6), (5, 6), (6, 6)
]

grid = GridMap(width, height, obstacles)

# -------------------------
# AGENTS
# -------------------------
agents = [
    Agent("LAND 1", 0, 0, speed=1),
    Agent("LAND 2", 1, 0, speed=1),
    Agent("LAND 3", 0, 1, speed=1),
]

# -------------------------
# GOAL
# -------------------------
goal = (5, 5)

# -------------------------
# PATH PLANNING
# -------------------------
paths = prioritized_astar(grid, agents, goal)

# -------------------------
# RESULTS
# -------------------------
for name, path in paths.items():
    print(f"{name} path: {path}")
    if path:
        print(f"{name} final: {path[-1]}")
    else:
        print(f"{name} final: NO MOVE")

# -------------------------
# FINAL MAP (ASCII)
# -------------------------
print("\nFINAL MAP VIEW:")
grid.render(agents=agents, goal=goal)

# -------------------------
# VISUAL MAP (MATPLOTLIB)
# -------------------------
print("\nVISUAL MAP:")
grid.render_visual(agents=agents, goal=goal)

print("=== SIMULATION END ===")
