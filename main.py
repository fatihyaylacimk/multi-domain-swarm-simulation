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


agents = [
    Agent("LAND 1", (0, 0), (5, 5), "LAND"),
    Agent("LAND 2", (1, 0), (1, 5), "LAND"),
    Agent("LAND 3", (0, 5), (9, 9), "LAND"),
    Agent("AIR 1",  (9, 0), (0, 9), "AIR"),
    Agent("AIR 2",  (9, 9), (0, 0), "AIR"),
]

for a in agents:
    if a.type == "LAND":
        a.set_path(simple_path(a.start, a.goal))

print("=== STEP-BY-STEP SIMULATION START ===")

step = 0
while True:
    print(f"\n--- STEP {step} ---")

    occupied = set(a.position for a in agents if not a.finished)

    # ---- AIR COMMUNICATION ----
    air_agents = [a for a in agents if a.type == "AIR" and not a.finished]
    air_plans = {}

    for air in sorted(air_agents, key=lambda a: a.name):
        plan = air.plan_next_air_move(occupied | set(air_plans.values()))
        air_plans[air.name] = plan

    active = False
    for agent in agents:
        pos = agent.move_step(occupied, air_plans)

        if agent.finished:
            print(f"{agent.name} finished")
        else:
            print(f"{agent.name} at {agent.position}")
            active = True

    if not active:
        break

    step += 1


print("\nFINAL MAP VIEW:")
final_map = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for a in agents:
    x, y = a.position
    final_map[y][x] = "A" if a.type == "AIR" else "L"

for row in final_map:
    print(" ".join(row))

print("=== SIMULATION END ===")
