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

    # LAND agents
    def set_path(self, path):
        self.path = path
        self.step_index = 0
        self.position = path[0]

    # Hareket (collision-aware)
    def move_step(self, occupied_positions=None):
        if self.finished:
            return None

        if occupied_positions is None:
            occupied_positions = set()

        # ---------- LAND ----------
        if self.type == "LAND":
            if self.step_index < len(self.path):
                next_pos = self.path[self.step_index]
                self.step_index += 1
                self.position = next_pos

                if self.position == self.goal:
                    self.finished = True

                return self.position
            else:
                self.finished = True
                return None

        # ---------- AIR (AKILLI) ----------
        if self.type == "AIR":
            x, y = self.position
            gx, gy = self.goal

            if (x, y) == (gx, gy):
                self.finished = True
                return None

            # Olası hareketler (8 yön – serbest uçuş)
            candidates = [
                (x + 1, y), (x - 1, y),
                (x, y + 1), (x, y - 1),
                (x + 1, y + 1), (x - 1, y - 1),
                (x + 1, y - 1), (x - 1, y + 1),
            ]

            # Hedefe yakınlığa göre sırala
            candidates.sort(
                key=lambda p: abs(p[0] - gx) + abs(p[1] - gy)
            )

            # Çakışmayan ilk hücreyi seç
            for nx, ny in candidates:
                if 0 <= nx < 10 and 0 <= ny < 10:
                    if (nx, ny) not in occupied_positions:
                        self.position = (nx, ny)
                        return self.position

            # Hiç yer yoksa bekle
            return self.position
