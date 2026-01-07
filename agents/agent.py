class Agent:
    def __init__(self, name, start, goal, agent_type, leader=None):
        self.name = name
        self.start = start
        self.goal = goal
        self.type = agent_type      # "LAND", "AIR_LEADER", "AIR_FOLLOWER"
        self.leader = leader
        self.position = start
        self.path = []
        self.step = 0
        self.finished = False

    def manhattan(self, p):
        return abs(p[0]-self.goal[0]) + abs(p[1]-self.goal[1])

    def plan(self, grid, forbidden):
        # Leader planlar
        if self.type != "AIR_LEADER":
            return

        x, y = self.position
        gx, gy = self.goal
        self.path = [(x, y)]

        while (x, y) != (gx, gy):
            candidates = []
            if x != gx:
                candidates.append((x + (1 if gx > x else -1), y))
            if y != gy:
                candidates.append((x, y + (1 if gy > y else -1)))

            candidates = [
                p for p in candidates
                if grid.in_bounds(*p) and p not in forbidden
            ]
            if not candidates:
                break

            best = min(candidates, key=self.manhattan)
            self.path.append(best)
            x, y = best

        self.step = 0

    def predict_next_positions(self, steps):
        return self.path[self.step:self.step+steps]

    def move(self, blocked, grid):
        if self.finished:
            return

        # FOLLOWER: liderin önceki konumunu takip et
        if self.type == "AIR_FOLLOWER":
            if self.leader:
                target = self.leader.position
                if target not in blocked:
                    self.position = target
            return

        # LEADER / LAND
        if self.step >= len(self.path):
            self.finished = True
            return

        next_pos = self.path[self.step]

        # Alternatif dene (AIR zekâsı)
        if self.type.startswith("AIR") and next_pos in blocked:
            x, y = self.position
            neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            neighbors = [
                p for p in neighbors
                if grid.in_bounds(*p) and p not in blocked
            ]
            if neighbors:
                next_pos = min(neighbors, key=self.manhattan)
            else:
                return  # bekle

        self.position = next_pos
        self.step += 1

        if self.position == self.goal:
            self.finished = True
