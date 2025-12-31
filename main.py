from cevre.harita import GridMap
from ajanlar.agent import Agent
from algoritmalar.prioritized_astar import prioritized_astar

print("=== SIMULATION START ===")

# GRID AYARLARI
width, height = 10, 10
obstacles = [(3,3), (3,4), (3,5), (4,5), (5,5)]
grid = GridMap(width, height, obstacles)

# HEDEF
goal = (8, 8)

# AJANLAR
agents = [
    Agent("LAND 1", 0, 0, speed=1),
    Agent("LAND 2", 0, 1, speed=1),
    Agent("LAND 3", 1, 0, speed=1),
]

# ARKA PLAN (İLK DURUM)
print("\nINITIAL MAP:")
grid.render(agents=agents, goal=goal)

# PLANLAMA
paths = prioritized_astar(grid, agents, goal)

# SONUÇLAR
for name, path in paths.items():
    print(f"{name} path: {path}")
    if path:
        print(f"{name} final: {path[-1]}")
    else:
        print(f"{name} final: NO MOVE")

# ARKA PLAN (SON DURUM)
print("\nFINAL MAP:")
grid.render(agents=agents, goal=goal)

print("=== SIMULATION END ===")
