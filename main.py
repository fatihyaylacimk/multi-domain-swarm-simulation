from agents.agent import Agent
from algorithms.air_path import air_path
from algorithms.prioritized_planning import prioritized_planning

GRID_SIZE = 10

obstacles = [
    (3, 3), (3, 4), (3, 5),
    (4, 5), (5, 5),
]

agents = [
    Agent("LAND 1", (0, 0), (5, 5), "LAND"),
    Agent("LAND 2", (1, 0), (1, 5), "LAND"),
    Agent("LAND 3", (0, 5), (9, 9), "LAND"),
    Agent("AIR 1",  (9, 0), (0, 9), "AIR"),   # ✈️
]

# LAND agents için prioritized planning
land_agents = [a for a in agents if a.type == "LAND"]
prioritized_planning(land_agents, GRID_SIZE, obstacles)

# AIR agent için serbest yol
for agent in agents:
    if agent.type == "AIR":
        agent.set_path(air_path(agent.start, agent.goal))

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

# FINAL MAP
print("\nFINAL MAP VIEW:")
grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for ox, oy in obstacles:
    grid[oy][ox] = "#"

for agent in agents:
    x, y = agent.position
    grid[y][x] = "A" if agent.type == "AIR" else "L"

for row in grid:
    print(" ".join(row))

print("=== SIMULATION END ===")
