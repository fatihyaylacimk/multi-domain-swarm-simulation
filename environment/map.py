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

    def render_gui(self, agents=None, goal=None):
        agents = agents if agents else []

        plt.figure(figsize=(6, 6))

        # Draw grid
        for x in range(self.width + 1):
            plt.plot([x, x], [0, self.height], color="gray", linewidth=0.5)
        for y in range(self.height + 1):
            plt.plot([0, self.width], [y, y], color="gray", linewidth=0.5)

        # Obstacles
        for (x, y) in self.obstacles:
            plt.fill_between([x, x + 1], y, y + 1, color="black")

        # Goal
        if goal:
            gx, gy = goal
            plt.scatter(gx + 0.5, gy + 0.5, c="green", s=200, label="Goal")

        # Agents
        for a in agents:
            plt.scatter(a.x + 0.5, a.y + 0.5, s=150, label=a.name)

        plt.xlim(0, self.width)
        plt.ylim(0, self.height)
        plt.gca().set_aspect("equal")
        plt.title("Multi-Domain Swarm Simulation")
        plt.legend()
        plt.grid(True)

        # 🔥 BU SATIR KRİTİK
        plt.show(block=True)
