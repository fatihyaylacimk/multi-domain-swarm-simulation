class GridMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def add_obstacle(self, x, y):
        self.grid[y][x] = 1

    def is_free(self, x, y):
        return self.grid[y][x] == 0
