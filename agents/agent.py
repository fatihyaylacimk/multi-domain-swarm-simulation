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

    def move(self, dx, dy, grid):
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < grid.width and 0 <= new_y < grid.height:
            if grid.is_free(new_x, new_y):
                self.x = new_x
                self.y = new_y
                self.status = "MOVING"
                return True

        self.status = "BLOCKED"
        return False
