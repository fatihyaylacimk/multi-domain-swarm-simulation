import matplotlib.pyplot as plt


class GridMap:
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.obstacles = obstacles if obstacles else []

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_free(self, x, y):
        return (x, y) not in self.obstacles

    def neighbors(self, x, y):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny) and self.is_free(nx, ny):
                result.append((nx, ny))
        return result

    # === TEXT MAP ===
    def render(self, agents=None, goal=None):
        agents = agents if agents else []

        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) in self.obstacles:
                    row += "# "
                elif goal and (x, y) == goal:
                    row += "G "
                elif any(a.x == x and a.y == y for a in agents):
                    row += "A "
                else:
                    row += ". "
            print(row)

    # === GUI MAP ===
    def render_gui(self, agents=None, goal=None):
        agents = agents if agents else []

        plt.figure(figsize=(6, 6))

        # Grid
        for x in range(self.width):
            for y in range(self.height):
                plt.scatter(x, y, c="white", edgecolors="black", s=400)

        # Obstacles
        for (x, y) in self.obstacles:
            plt.scatter(x, y, c="black", s=400)

        # Goal
        if goal:
            plt.scatter(goal[0], goal[1], c="green", s=400, label="Goal")

        # Agents
        colors = ["red", "blue", "orange", "purple"]
        for i, agent in enumerate(agents):
            plt.scatter(agent.x, agent.y, c=colors[i % len(colors)], s=400, label=agent.name)

        plt.title("Multi-Domain Swarm Simulation")
        plt.xlim(-1, self.width)
        plt.ylim(-1, self.height)
        plt.gca().set_aspect("equal")
        plt.grid(True)
        plt.legend()
        plt.show()
plt.show(block=True)

from map import GridMap
from algorithms.prioritized_astar import prioritized_astar

def main():
    print("=== SIMULATION START ===")

    # Grid ayarları
    width = 10
    height = 10

    obstacles = [
        (2, 2), (2, 3), (2, 4),
        (4, 6), (5, 6), (6, 6)
    ]

    grid = GridMap(width, height, obstacles)

    # Hedef
    goal = (5, 5)

    # Agent başlangıç noktaları
    agents = [
        {"name": "LAND 1", "start": (0, 0)},
        {"name": "LAND 2", "start": (1, 8)},
        {"name": "LAND 3", "start": (8, 1)},
    ]

    all_paths = []

    for agent in agents:
        path = prioritized_astar(
            grid=grid,
            start=agent["start"],
            goal=goal,
            reserved_paths=all_paths
        )

        if path:
            print(f"{agent['name']} path: {path}")
            print(f"{agent['name']} final: {path[-1]}")
            all_paths.append(path)
        else:
            print(f"{agent['name']} -> NO PATH FOUND")
            print(f"{agent['name']} final: NO MOVE")
            all_paths.append([])

    print("\nFINAL MAP VIEW:")
    grid.render(
        agents=[type("A", (), {"x": p[-1][0], "y": p[-1][1]})
                for p in all_paths if p],
        goal=goal
    )

    print("=== SIMULATION END ===")

    # >>> GUI AÇILAN KISIM (ÖNEMLİ) <<<
    print("GUI OPENING...")
    grid.render_gui(
        agents=[type("A", (), {"x": p[-1][0], "y": p[-1][1]})
                for p in all_paths if p],
        goal=goal
    )

import matplotlib.pyplot as plt
plt.show(block=True)

