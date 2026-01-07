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

    def plan(self, grid, forbidden):
        if self.type != "AIR":
            return

        # Basit Manhattan A* benzeri yol
        x, y = self.position
        gx, gy = self.goal
        self.path = [(x, y)]

        while x != gx:
            x += 1 if gx > x else -1
            if (x, y) in forbidden:
                break
            self.path.append((x, y))

        while y != gy:
            y += 1 if gy > y else -1
            if (x, y) in forbidden:
                break
            self.path.append((x, y))

        self.step = 0

    def predict_next_positions(self, steps):
        future = []
        for i in range(self.step, min(self.step + steps, len(self.path))):
            future.append(self.path[i])
        return future

    def move(self, blocked_positions=None):
        if self.finished:
            return

        if self.step >= len(self.path):
            self.finished = True
            return

        next_pos = self.path[self.step]

        if blocked_positions and next_pos in blocked_positions:
            return  # BEKLE

        self.position = next_pos
        self.step += 1

        if self.position == self.goal:
            self.finished = True
