# =========================
# main.py
# Multi-Domain Swarm Simulation
# =========================

from map import GridMap
import heapq
import time


# -------------------------
# A* PATHFINDING
# -------------------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))

    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for nx, ny in grid.neighbors(*current):
            new_cost = cost_so_far[current] + 1
            next_node = (nx, ny)

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal, next_node)
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current

    if goal not in came_from:
        return []

    # Path reconstruction
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = came_from[cur]
    path.reverse()
    return path


# -------------------------
# AGENT CLASS
# -------------------------
class Agent:
    def __init__(self, name, x, y, goal):
        self.name = name
        self.x = x
        self.y = y
        self.goal = goal
        self.path = []

    def compute_path(self, grid):
        self.path = astar(grid, (self.x, self.y), self.goal)

    def move(self):
        if len(self.path) > 1:
            self.path.pop(0)
            self.x, self.y = self.path[0]


# -------------------------
# MAIN SIMULATION
# -------------------------
def run_simulation():
    width, height = 10, 10
    obstacles = [(3, 3), (3, 4), (3, 5), (6, 6), (7, 6)]
    goal = (8, 8)

    grid = GridMap(width, height, obstacles)

    agents = [
        Agent("LAND 1", 0, 0, goal),
        Agent("LAND 2", 0, 5, goal),
        Agent("LAND 3", 5, 0, goal),
    ]

    print("=== SIMULATION START ===")

    for agent in agents:
        agent.compute_path(grid)
        if agent.path:
            print(f"{agent.name} path: {agent.path}")
        else:
            print(f"{agent.name} -> NO PATH FOUND")

    # STEP-BY-STEP MOVEMENT
    for _ in range(20):
        for agent in agents:
            agent.move()
        time.sleep(0.2)

    print("=== SIMULATION END ===")

    # FINAL GUI RENDER
    grid.render_gui(agents=agents, goal=goal)


# -------------------------
# ENTRY POINT
# -------------------------
if __name__ == "__main__":
    run_simulation()

print("GUI OPENING...")
grid.render_gui(agents=agents, goal=goal)

