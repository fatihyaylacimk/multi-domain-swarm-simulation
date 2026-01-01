import heapq

# -----------------------------
# A* PATHFINDING
# -----------------------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, neighbor))

    return []

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
# GRID (SABİT)
# -----------------------------
GRID_SIZE = 10
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

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
    agent.path = astar(grid, agent.start, agent.goal)

    if agent.path:
        agent.final = agent.path[-1]
        print(f"{agent.name} path: {agent.path}")
        print(f"{agent.name} final: {agent.final}")
    else:
        agent.final = "NO MOVE"
        print(f"{agent.name} -> NO PATH FOUND")
        print(f"{agent.name} path: []")
        print(f"{agent.name} final: NO MOVE")

# -----------------------------
# FINAL MAP VIEW
# -----------------------------
print("\nFINAL MAP VIEW:")

final_map = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for agent in agents:
    if agent.final != "NO MOVE":
        r, c = agent.final
        final_map[r][c] = "L"

for row in final_map:
    print(" ".join(row))

print("=== SIMULATION END ===")
