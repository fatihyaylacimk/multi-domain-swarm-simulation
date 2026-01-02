class Agent:
    def __init__(self, name, start, goal):
        self.name = name
        self.start = start
        self.goal = goal
        self.path = []
        self.step_index = 0
        self.position = start
        self.wait = False

    def set_path(self, path):
        self.path = path
        self.step_index = 0
        self.position = self.start

    def peek_next(self):
        if self.step_index < len(self.path):
            return self.path[self.step_index]
        return None

    def move_step(self):
        if self.step_index < len(self.path):
            self.position = self.path[self.step_index]
            self.step_index += 1
            return self.position
        return None

    def finished(self):
        return self.step_index >= len(self.path)
