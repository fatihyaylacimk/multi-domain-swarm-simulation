class Agent:
    def __init__(self, name, start, goal, agent_type):
        self.name = name
        self.start = start
        self.goal = goal
        self.type = agent_type
        self.path = []
        self.position = start
        self.step = 0
        self.finished = False

    def manhattan(self, p):
        return abs(p[0] - self.goal[0]) + abs(p[1] - self.goal[1])

    def plan(self, grid, forbidden):
        if self.type != "AIR":
            return

        x, y = self.position
        gx, gy = self.goal
        self.path = [(x, y)]

        while (x, y) != (gx, gy):
            options = []

            if x != gx:
                nx = x + (1 if gx > x else -1)
                options.append((nx, y))
            if y != gy:
                ny = y + (1 if gy > y else -1)
                options.append((x, ny))

            options = [p for p in options if p not in forbidden]

            if not options:
                break

            best = min(options, key=self.manhattan)
            self.path.append(best)
            x, y = best

        self.step = 0

    def predict_next_positions(self, steps):
        return self.path[self.step:self.step+steps]

    def move(self, blocked_positions, grid):
        if self.finished:
            return

        if self.step >= len(self.path):
            self.finished = True
            return

        next_pos = self.path[self.step]

        # 🔁 Alternatif yol dene
        if next_pos in blocked_positions:
            x, y = self.position
            candidates = [
                (x+1,y),(x-1,y),(x,y+1),(x,y-1)
            ]
            candidates = [
                p for p in candidates
                if grid.in_bounds(*p) and p not in blocked_positions
            ]

            if candidates:
                next_pos = min(candidates, key=self.manhattan)
            else:
                return  # BEKLE

        self.position = next_pos
        self.step += 1

        if self.position == self.goal:
            self.finished = True
