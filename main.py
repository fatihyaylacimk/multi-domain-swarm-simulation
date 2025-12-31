import time

from environment.map import GridMap
from agents.agent import Agent
from algorithms.prioritized_astar import prioritized_astar

# ======================
# SIMULATION SETUP
# ======================
print("=== SIMULATION START ===")

grid = GridMap(
    width=10,
    height=10,
    obstacles=[]
)

agents = [
    Agent("LAND 1", 0, 0, speed=1),
    Agent("LAND 2", 1, 0, speed=1),
    Agent("LAND 3", 2, 0, speed=1),
]

goal = (5, 5)

# ======================
# PATH PLANNING
# ======================
paths = prioritized_astar(grid, agents, goal)

for name, path in paths.items():
    if path:
        print(f"{name} path: {path}")
    else:
        print(f"{name} -> NO PATH FOUND")

# ======================
# ADIM ADIM SIMULATION
# ======================
max_steps = max(len(p) for p in paths.values())

for step in range(max_steps):
    print(f"\n--- STEP {step} ---")

    for agent in agents:
        path = paths.get(agent.name, [])

        if step < len(path):
            x, y = path[step]
            agent.x = x
            agent.y = y

    grid.render_visual(agents=agents, goal=goal)
    time.sleep(0.6)

# ======================
# FINAL STATE
# ======================
print("\n=== SIMULATION END ===")
