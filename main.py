print("### NEW MAIN.PY RUNNING ###")

GRID_SIZE = 10

# -----------------------------
# SADE PATH (ENGELSİZ)
# -----------------------------
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

# -----------------------------
# AGENT
# -----------------------------
class Agent:
    def __init__(self, name, start, goal):
        self.name = name
        self.start = start
        self.goal = goal
        self.path = []
        self.final = None

# -----------------------------
# AGENTS
# -----------------------------
agents = [
    Agent("LAND 1", (0, 0), (5, 5)),
    Agent("LAND 2", (1, 0), (1, 5)),
    Agent("LAND 3", (0, 5), (9, 9)),
]

# -----------------------------
# SIMULATION
# -----------------------------
print("=== SIMULATION START ===")

for agent in agents:
    agent.path = simple_path(agent.start, agent.goal)
    agent.final = agent.path[-1]

    print(f"{agent.name} path: {agent.path}")
    print(f"{agent.name} final: {agent.final}")

# -----------------------------
# FINAL MAP
# -----------------------------
print("\nFINAL MAP VIEW:")

final_map = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for agent in agents:
    x, y = agent.final
    final_map[y][x] = "L"

for row in final_map:
    print(" ".join(row))

print("=== SIMULATION END ===")
