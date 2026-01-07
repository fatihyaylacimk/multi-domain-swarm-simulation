from agents.agent import Agent

class Grid:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def in_bounds(self, x, y):
        return 0 <= x < self.w and 0 <= y < self.h

grid = Grid(10, 10)

# LAND'ler
land1 = Agent("LAND 1", (0,0), (5,5), "LAND")
land1.path = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)]

# AIR Swarm
air_leader = Agent("AIR L", (2,2), (9,9), "AIR_LEADER")
air_follower = Agent("AIR F", (2,1), None, "AIR_FOLLOWER", leader=air_leader)

agents = [land1, air_leader, air_follower]

# Leader planlasın
air_leader.plan(grid, forbidden=set())

print("=== STEP-BY-STEP SIMULATION START ===")
for step in range(15):
    print(f"\n--- STEP {step} ---")
    blocked = {a.position for a in agents}

    for a in agents:
        a.move(blocked, grid)
        print(f"{a.name} at {a.position}")

print("=== SIMULATION END ===")
