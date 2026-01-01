print("### STEP-BY-STEP AGENT MOVE ###")

from agents.agent import Agent

GRID_SIZE = 10

def simple_path(start, goal):
    x, y = start
    gx, gy = goal
    path = []

    while (x, y) != (gx, gy):
        path.append((x, y))
        if x != gx:
            x += 1 if gx > x else -1
        elif y != gy:
            y += 1 if gy > y else -1

    path.append((gx, gy))
    return path


agents = [
    Agent("LAND 1", (0, 0), (5, 5)),
    Agent("LAND 2", (1, 0), (1, 5)),
    Agent("LAND 3", (0, 5), (9, 9)),
]

# Path ata
for agent in agents:
    agent.set_path(simple_path(agent.start, agent.goal))

print("=== SIMULATION START ===")

finished = False
step = 0

while not finished:
    print(f"\nSTEP {step}")
    finished = True

    grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for agent in agents:
        if not agent.reached_goal():
            agent.move()
            finished = False

        x, y = agent.position()
        grid[y][x] = "L"

        print(f"{agent.name} -> {agent.position()}")

    for row in grid:
        print(" ".join(row))

    step += 1

print("\n=== SIMULATION END ===")
