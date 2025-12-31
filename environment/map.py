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

        print("\nFINAL MAP VIEW:")
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
