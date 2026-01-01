print("### AGENT.PY LOADED ###")





class Agent:
    def __init__(self, name, start, goal):
        self.name = name
        self.start = start
        self.goal = goal
        self.path = []
        self.final = None

    def set_path(self, path):
        self.path = path
        if path:
            self.final = path[-1]
        else:
            self.final = None
