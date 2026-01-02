from agents.agent import Agent
from algorithms.astar import astar

GRID_SIZE = 10

# ENGELLER (istersen ekle)
obstacles = [
    (3, 3), (3, 4), (3, 5),
    (4, 5), (5, 5),
]

agents = [
    Agent("LAND 1", (0, 0), (5, 5)),
    Agent("LAND 2", (1, 0), (1, 5)),
    Agent("LAND 3", (0, 5), (9, 9)),
]

# A* ile path üret
for agent in agents:
    path = astar(agent.start, agent.goal, GRID_SIZE, obstacles)
    agent.set_path(path)

print("=== STEP-BY-STEP SIMULATION START ===")

step = 0
while True:
    print(f"\n--- STEP {step} ---")

    next_positions = {}
    active_agents = 0

    # ÇAKIŞMA KONTROLÜ
    for agent in agents:
        if agent.finished():
            continue

        active_agents += 1
        nxt = agent.peek_next()
        if nxt is None:
            continue

        if nxt not in next_positions:
            next_positions[nxt] = agent
        else:
            agent.wait = True

    # HAREKET
    for agent in agents:
        if agent.finished():
            print(f"{agent.name} finished")
            continue

        if agent.wait:
            print(f"{agent.name} WAIT at {agent.position}")
            agent.wait = False
        else:
            agent.move_step()
            print(f"{agent.name} at {agent.position}")

    if active_agents == 0:
        break

    step += 1

# FINAL MAP
print("\nFINAL MAP VIEW:")
grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for ox, oy in obstacles:
    grid[oy][ox] = "#"

for agent in agents:
    x, y = agent.position
    grid[y][x] = "L"

for row in grid:
    print(" ".join(row))

print("=== SIMULATION END ===")
