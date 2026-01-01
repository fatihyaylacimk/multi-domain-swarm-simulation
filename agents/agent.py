class Agent:
    def __init__(self, name, start, goal):
        self.name = name
        self.start = start
        self.goal = goal
        self.path = []
        self.final = None
        self.step_index = 0

    def set_path(self, path):
        self.path = path
        self.step_index = 0
        if path:
            self.final = path[-1]
        else:
            self.final = None

    def move_step(self):
        if self.step_index < len(self.path):
            pos = self.path[self.step_index]
            self.step_index += 1
            return pos
        return None
