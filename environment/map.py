    def render(self, agents=None, goal=None):
        view = [[ "." for _ in range(self.width)] for _ in range(self.height)]

        # engeller
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    view[y][x] = "#"

        # hedef
        if goal:
            gx, gy = goal
            view[gy][gx] = "G"

        # agentlar
        if agents:
            for a in agents:
                x, y = a.position()
                view[y][x] = "A" if a.agent_type == "LAND" else "H"

        for row in view:
            print(" ".join(row))
        print()
