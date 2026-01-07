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

    # LAND agents için
    def set_path(self, path):
        self.path = path
        self.step_index = 0
        self.position = path[0]

    # AIR agent için – akıllı 2D hareket
    def move_step(self):
        if self.finished:
            return None

        # LAND agent
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

        # AIR agent (serbest 2D akıllı hareket)
        if self.type == "AIR":
            x, y = self.position
            gx, gy = self.goal

            if (x, y) == (gx, gy):
                self.finished = True
                return None

            if x < gx:
                x += 1
            elif x > gx:
                x -= 1

            if y < gy:
                y += 1
            elif y > gy:
                y -= 1

            self.position = (x, y)
            return self.position
