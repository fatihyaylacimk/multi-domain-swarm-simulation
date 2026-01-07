from agents.agent import Agent

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


# === AGENTS ===
agents = [
    Agent("LAND 1", (0, 0), (5, 5), "LAND"),
    Agent("LAND 2", (1, 0), (1, 5), "LAND"),
    Agent("LAND 3", (0, 5), (9, 9), "LAND"),
    Agent("AIR 1",  (9, 0), (0, 9), "AIR"),
]

# LAND path setup
for agent in agents:
    if agent.type == "LAND":
        agent.set_path(simple_path(agent.start, agent.goal))

print("=== STEP-BY-STEP SIMULATION START ===")

step = 0
while True:
    print(f"\n--- STEP {step} ---")
    active = False

    for agent in agents:
        pos = agent.move_step()

        if agent.finished:
            print(f"{agent.name} finished")
        else:
            print(f"{agent.name} at {agent.position}")
            active = True

    if not active:
        break

    step += 1

# === FINAL MAP ===
print("\nFINAL MAP VIEW:")
final_map = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for agent in agents:
    x, y = agent.position
    final_map[y][x] = "A" if agent.type == "AIR" else "L"

for row in final_map:
    print(" ".join(row))

print("=== SIMULATION END ===")
