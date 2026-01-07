from agents.agent import Agent

GRID_SIZE = 10


# --------------------
# LAND PATH (4 yön)
# --------------------
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


# --------------------
# AIR PATH (2D SERBEST – ÇAPRAZ)
# --------------------
def air_free_path(start, goal):
    x, y = start
    gx, gy = goal
    path = [(x, y)]

    while (x, y) != (gx, gy):
        if x < gx:
            x += 1
        elif x > gx:
            x -= 1

        if y < gy:
            y += 1
        elif y > gy:
            y -= 1

        path.append((x, y))

    return path


# --------------------
# AGENTS
# --------------------
land1 = Agent("LAND 1", (0, 0), (5, 5), agent_type="LAND", speed=1)
land2 = Agent("LAND 2", (1, 0), (1, 5), agent_type="LAND", speed=1)
land3 = Agent("LAND 3", (0, 5), (9, 9), agent_type="LAND", speed=1)

air_leader = Agent("AIR L", (9, 0), (5, 5), agent_type="AIR", speed=2)
air_follower = Agent(
    "AIR F",
    (9, 1),
    None,
    agent_type="AIR_FOLLOWER",
    speed=2,
    leader=air_leader
)

agents = [land1, land2, land3, air_leader, air_follower]


# --------------------
# PATH ATAMA
# --------------------
for a in agents:
    if a.goal:
        if "AIR" in a.type:
            a.set_path(air_free_path(a.start, a.goal))
        else:
            a.set_path(simple_path(a.start, a.goal))


# --------------------
# SIMULATION
# --------------------
print("=== STEP-BY-STEP SIMULATION START ===")

step = 0
while True:
    print(f"\n--- STEP {step} ---")

    occupied = set(a.position for a in agents if not a.finished)
    reserved = set()

    all_finished = True

    for agent in agents:
        if agent.finished:
            print(f"{agent.name} finished")
            continue

        agent.move(blocked=occupied | reserved, grid=None)
        reserved.add(agent.position)

        print(f"{agent.name} at {agent.position}")
        all_finished = False

    if all_finished:
        break

    step += 1


# --------------------
# FINAL MAP
# --------------------
print("\nFINAL MAP VIEW:")
final_map = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for a in agents:
    x, y = a.position
    symbol = "A" if "AIR" in a.type else "L"
    final_map[y][x] = symbol

for row in final_map:
    print(" ".join(row))

print("=== SIMULATION END ===")
