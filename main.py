from agents.agent import Agent

GRID_SIZE = 10

def simple_path(start, goal):
    x, y = start
    gx, gy = goal
    path = []

    while x != gx:
        path.append((x, y))
        x += 1 if gx > x else -1

    while y != gy:
        path.append((x, y))
        y += 1 if gy > y else -1

    path.append((gx, gy))
    return path


agents = [
    Agent("LAND 1", (0, 0), (5, 5)),
    Agent("LAND 2", (1, 0), (1, 5)),
    Agent("LAND 3", (0, 5), (9, 9)),
]

for agent in agents:
    agent.set_path(simple_path(agent.start, agent.goal))

print("=== STEP-BY-STEP SIMULATION START ===")

step = 0
while True:
    print(f"\n--- STEP {step} ---")

    next_positions = {}
    active_agents = 0

    # 1️⃣ ÇAKIŞMA KONTROLÜ
    for agent in agents:
        if agent.finished():
            continue

        active_agents += 1
        next_pos = agent.peek_next()

        if next_pos not in next_positions:
            next_positions[next_pos] = agent
        else:
            agent.wait = True

    # 2️⃣ HAREKET
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

for agent in agents:
    x, y = agent.position
    grid[y][x] = "L"

for row in grid:
    print(" ".join(row))

print("=== SIMULATION END ===")
