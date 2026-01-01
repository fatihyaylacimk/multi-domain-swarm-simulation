print(Agent)





from agents.agent import Agent



from agents.agent import Agent
import time

from agents.agent import Agent

print("AGENT CLASS FROM:", Agent.__module__)
print("AGENT FILE:", Agent.__dict__.get('__file__', 'NO FILE INFO'))
print("HAS set_path:", hasattr(Agent, "set_path"))







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
    Agent("LAND 1", (0, 0), (5, 5)),
    Agent("LAND 2", (1, 0), (1, 5)),
    Agent("LAND 3", (0, 5), (9, 9)),
]

for agent in agents:
    agent.set_path(simple_path(agent.start, agent.goal))

print("=== STEP-BY-STEP SIMULATION START ===")

max_steps = max(len(a.path) for a in agents)

for step in range(max_steps):
    print(f"\n--- STEP {step} ---")

    grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for agent in agents:
        x, y = agent.move_step()
        grid[y][x] = "L"
        print(f"{agent.name} at {agent.position}")

    for row in grid:
        print(" ".join(row))

    time.sleep(0.5)

print("\n=== SIMULATION END ===")
