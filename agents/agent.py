class Agent:
    def __init__(self, name, start, goal, agent_type="LAND"):
        self.name = name
        self.start = start
        self.goal = goal
        self.type = agent_type   # LAND / AIR
        self.path = []
        self.position = start
        self.step_index = 0

    def set_path(self, path):
        self.path = path
        self.step_index = 0
        self.position = self.start

    def move_step(self):
        if self.step_index < len(self.path):
            self.position = self.path[self.step_index]
            self.step_index += 1
            return self.position
        return None

    def finished(self):
        return self.step_index >= len(self.path)
