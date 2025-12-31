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
