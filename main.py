print("=== STEP-BY-STEP SIMULATION START ===")

GRID_SIZE = 10


def simple_path(start, goal):
    x, y = start
    gx, gy = goal
    path = [(x, y)]

    while x != gx:
        x += 1 if gx > x else -1
        path.append((x, y))

    while y != gy:
        y += 1 if gy > y else -1
        path.append((x, y))

    return path


# IMPORT AGENT
from agents.agent import Agent


# CREATE AGENTS
agents = [
    Agent("LAND 1", (0, 0), (5, 5)),
    Agent("LAND 2", (1, 0), (1, 5)),
    Agent("LAND 3", (0, 5), (9, 9)),
]


# ASSIGN PATHS
for agent in agents:
    path = simple_path(agent.start, agent.goal)
    agent.set_path(path)


# STEP-BY-STEP SIMULATION
max_steps = max(len(agent.path) for agent in agents)

for step in range(max_steps):
    print(f"\n--- STEP {step} ---")

    for agent in agents:
        pos = agent.move_step()
        if pos is not None:
            print(f"{agent.name} at {pos}")
        else:
            print(f"{agent.name} has finished")


# FINAL MAP VIEW
print("\nFINAL MAP VIEW:")
final_map = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for agent in agents:
    if agent.final:
        x, y = agent.final
        final_map[y][x] = "L"

for row in final_map:
    print(" ".join(row))

print("=== SIMULATION END ===")
