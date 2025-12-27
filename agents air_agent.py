from agents.agent import Agent

class AirAgent(Agent):
    def __init__(self, agent_id, x, y, speed):
        super().__init__(agent_id, "AIR", x, y, speed)

    # Hava agent engelleri yok sayabilir (basit model)
    def move(self, dx, dy, grid):
        self.x += dx
        self.y += dy
        self.status = "MOVING"
        return True
