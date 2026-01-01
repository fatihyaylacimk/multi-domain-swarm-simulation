class Agent:
    def __init__(self, name, start, goal):
        self.name = name
        self.start = start
        self.goal = goal
        self.path = []
        self.final = None
        self.current_index = 0
        self.position = start

    def set_path(self, path):
        self.path = path
        self.current_index = 0
        self.position = self.start

    def move_step(self):
        if self.current_index < len(self.path):
            self.position = self.path[self.current_index]
            self.current_index += 1
            return self.position
        return self.position
