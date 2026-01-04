from agents.agent import Agent

GRID_SIZE = 10


def simple_land_path(start, goal):
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


def simple_air_path(start, goal):
    x, y = start
    gx, gy = goal
    path = [(x, y)]

    while x != gx or y != gy:
        if x != gx:
            x += 1 if gx > x else -1
        if y != gy:
            y += 1 if gy > y else -1
        path.append((x, y))

    return path


agents = [
    Agent("LAND 1", (0, 0), (5, 5), "LAND"),
    Agent("LAND 2", (1, 0), (1, 5), "LAND"),
    Agent("LAND 3", (0, 5), (9, 9), "LAND"),
    Agent("AIR 1", (9, 0), (0, 9), "AIR"),
]

for agent in agents:
    if agent.type == "LAND":
        agent.set_path(simple_land_path(agent.start, agent.goal))
    else:
        agent.set_path(simple_air_path(agent.start, agent.goal))


print("=== STEP-BY-STEP SIMULATION START ===\n")

step = 0
running = True

while running:
    print(f"--- STEP {step} ---")
    running = False

    for agent in agents:
        if not agent.finished():
            agent.move_step()
            print(f"{agent.name} at {agent.position}")
            running = True
        else:
            print(f"{agent.name} finished")

    print()
    step += 1


print("FINAL MAP VIEW:")
final_map = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for agent in agents:
    x, y = agent.position
    final_map[y][x] = "A" if agent.type == "AIR" else "L"

for row in final_map:
    print(" ".join(row))

print("=== SIMULATION END ===")
