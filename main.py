from agents.agent import Agent
from algorithms.air_path import air_path

GRID_SIZE = 10

agents = [
    Agent("LAND 1", (0, 0), (5, 5), "LAND"),
    Agent("LAND 2", (1, 0), (1, 5), "LAND"),
    Agent("LAND 3", (0, 5), (9, 9), "LAND"),
    Agent("AIR 1",  (9, 0), (0, 9), "AIR"),   # ✈️ AIR
]

def simple_path(start, goal):
    x, y = start
    gx, gy = goal
    path = []

    while x != gx:
        x += 1 if gx > x else -1
        path.append((x, y))

    while y != gy:
        y += 1 if gy > y else -1
        path.append((x, y))

    return path

# Path atama
for agent in agents:
    if agent.type == "AIR":
        agent.set_path(air_path(agent.start, agent.goal))
    else:
        agent.set_path(simple_path(agent.start, agent.goal))

print("=== STEP-BY-STEP SIMULATION START ===")

step = 0
while True:
    print(f"\n--- STEP {step} ---")
    active = 0

    for agent in agents:
        if agent.finished():
            print(f"{agent.name} finished")
            continue

        active += 1
        agent.move_step()
        print(f"{agent.name} at {agent.position}")

    if active == 0:
        break

    step += 1

print("\nFINAL MAP VIEW:")
grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for agent in agents:
    x, y = agent.position
    grid[y][x] = "A" if agent.type == "AIR" else "L"

for row in grid:
    print(" ".join(row))

print("=== SIMULATION END ===")
