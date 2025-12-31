import matplotlib.pyplot as plt


class GridMap:
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.obstacles = obstacles if obstacles else []

        # GUI için tek pencere kullanacağız
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(6, 6))

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

    def render_gui(self, agents=None, goal=None):
        agents = agents if agents else []

        self.ax.clear()
        self.ax.set_title("Multi-Domain Swarm Simulation")

        # Grid ayarları
        self.ax.set_xlim(-0.5, self.width - 0.5)
        self.ax.set_ylim(-0.5, self.height - 0.5)
        self.ax.set_xticks(range(self.width))
        self.ax.set_yticks(range(self.height))
        self.ax.grid(True)
        self.ax.invert_yaxis()

        # Obstacles
        for (x, y) in self.obstacles:
            self.ax.scatter(x, y, c="black", s=300)

        # Goal
        if goal:
            self.ax.scatter(goal[0], goal[1], c="green", s=300, marker="*")

        # Agents
        for agent in agents:
            self.ax.scatter(agent.x, agent.y, c="blue", s=150)
            self.ax.text(agent.x + 0.1, agent.y + 0.1, agent.name, fontsize=8)

        plt.pause(0.3)
