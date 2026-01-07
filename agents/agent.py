from algorithms.astar import astar

class Agent:
    def __init__(self, name, start, goal, agent_type):
        self.name = name
        self.start = start
        self.goal = goal
        self.type = agent_type

        self.position = start
        self.path = []
        self.step = 0
        self.memory = set()   # AIR learning
        self.finished = False

    def plan(self, grid, forbidden):
        if self.type == "AIR":
            self.path = astar(grid, self.position, self.goal, forbidden | self.memory)
            self.step = 0

    def move(self):
        if self.finished:
            return

        if self.step < len(self.path):
            self.position = self.path[self.step]
            self.step += 1
            if self.position == self.goal:
                self.finished = True
        else:
            self.finished = True
