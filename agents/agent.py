class Agent:
    def __init__(self, name, start, goal, agent_type="LAND", speed=1, leader=None):
        self.name = name
        self.start = start
        self.position = start
        self.goal = goal
        self.type = agent_type  # LAND, AIR, AIR_FOLLOWER
        self.speed = speed
        self.leader = leader

        self.path = []
        self.step = 0
        self.finished = False

    def set_path(self, path):
        self.path = path
        self.step = 0
        self.position = self.start
        self.finished = False

    def move(self, blocked, grid):
        if self.finished:
            return

        # AIR FOLLOWER: lideri aynen takip eder
        if self.type == "AIR_FOLLOWER" and self.leader:
            self.position = self.leader.position
            return

        for _ in range(self.speed):
            if self.step >= len(self.path):
                self.finished = True
                return

            next_pos = self.path[self.step]

            # ÇARPIŞMA KONTROLÜ
            if next_pos in blocked:
                # AIR bekler, LAND zaten giremez
                return

            self.position = next_pos
            self.step += 1

            if self.position == self.goal:
                self.finished = True
                return
