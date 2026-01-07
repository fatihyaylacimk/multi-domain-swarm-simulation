class GridMap:
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles) if obstacles else set()

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def is_free(self, pos):
        return pos not in self.obstacles

    def neighbors(self, pos):
        x, y = pos
        moves = [
            (x+1,y),(x-1,y),(x,y+1),(x,y-1),
            (x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)
        ]
        return [m for m in moves if self.in_bounds(m) and self.is_free(m)]
