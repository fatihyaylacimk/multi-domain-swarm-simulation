class Agent:
    def __init__(self, name, start, goal, agent_type="LAND"):
        self.name = name
        self.start = start
        self.goal = goal
        self.type = agent_type

        self.path = []
        self.step_index = 0
        self.position = start
        self.finished = False

    def set_path(self, path):
        self.path = path
        self.step_index = 0
        self.position = path[0]

    def plan_next_air_move(self, occupied):
        x, y = self.position
        gx, gy = self.goal

        candidates = [
            (x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1),
            (x + 1, y + 1), (x - 1, y - 1),
            (x + 1, y - 1), (x - 1, y + 1),
        ]

        candidates = [
            p for p in candidates
            if 0 <= p[0] < 10 and 0 <= p[1] < 10
        ]

        candidates.sort(
            key=lambda p: abs(p[0] - gx) + abs(p[1] - gy)
        )

        for c in candidates:
            if c not in occupied:
                return c

        return self.position  # bekle

    def move_step(self, occupied_positions=None, air_plans=None):
        if self.finished:
            return None

        if occupied_positions is None:
            occupied_positions = set()

        # -------- LAND --------
        if self.type == "LAND":
            if self.step_index < len(self.path):
                self.position = self.path[self.step_index]
                self.step_index += 1
                if self.position == self.goal:
                    self.finished = True
                return self.position
            else:
                self.finished = True
                return None

        # -------- AIR --------
        if self.type == "AIR":
            if self.position == self.goal:
                self.finished = True
                return None

            next_pos = air_plans.get(self.name, self.position)
            self.position = next_pos
            return self.position
