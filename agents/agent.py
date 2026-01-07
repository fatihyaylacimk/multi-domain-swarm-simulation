class Agent:
    def __init__(self, name, start, goal, agent_type, leader=None):
        self.name = name
        self.start = start
        self.goal = goal
        self.type = agent_type          # "LAND", "AIR_LEADER", "AIR_FOLLOWER"
        self.leader = leader

        self.position = start
        self.path = []
        self.step = 0
        self.finished = False

        # 🔴 AIR özellikleri
        self.can_fly = self.type.startswith("AIR")
        self.speed = 2 if self.can_fly else 1   # 🔴 HIZ FARKI

    def manhattan(self, p):
        return abs(p[0]-self.goal[0]) + abs(p[1]-self.goal[1])

    def plan(self, grid, forbidden):
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

            # AIR engel umursamaz
            if not self.can_fly:
                candidates = [p for p in candidates if p not in forbidden]

            candidates = [p for p in candidates if grid.in_bounds(*p)]
            if not candidates:
                break

            best = min(candidates, key=self.manhattan)
            self.path.append(best)
            x, y = best

        self.step = 0

    def move(self, blocked, grid):
        if self.finished:
            return

        # FOLLOWER: lideri kopyala
        if self.type == "AIR_FOLLOWER" and self.leader:
            self.position = self.leader.position
            return

        # 🔴 HIZ KULLANIMI
        for _ in range(self.speed):
            if self.step >= len(self.path):
                self.finished = True
                return

            next_pos = self.path[self.step]

            # LAND çarpışma, AIR uçabilir
            if not self.can_fly and next_pos in blocked:
                return

            self.position = next_pos
            self.step += 1

            if self.goal and self.position == self.goal:
                self.finished = True
                return
