class Agent:
    def __init__(self, agent_id, agent_type, x, y, speed):
        self.agent_id = agent_id
        self.agent_type = agent_type  # AIR or LAND
        self.x = x
        self.y = y
        self.speed = speed
        self.status = "IDLE"

    def position(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.status = "MOVING"
