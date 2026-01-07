from agents.agent import Agent

class Grid:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def in_bounds(self, x, y):
        return 0 <= x < self.w and 0 <= y < self.h

grid = Grid(10, 10)

# 🔴 Engel tanımı
obstacles = {(4,4), (5,4), (6,4)}

# LAND
land = Agent("LAND", (0,0), (8,8), "LAND")
land.path = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
             (8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8)]

# AIR swarm
air_leader = Agent("AIR L", (2,2), (8,8), "AIR_LEADER")
air_follower = Agent("AIR F", (2,1), None, "AIR_FOLLOWER", leader=air_leader)

agents = [land, air_leader, air_follower]

# AIR lider planlasın (engel umursamaz)
air_leader.plan(grid, forbidden=obstacles)

print("=== AIR ALTITUDE SIMULATION START ===")
for step in range(15):
    print(f"\n--- STEP {step} ---")
    blocked = obstacles | {a.position for a in agents}

    for a in agents:
        a.move(blocked, grid)
        print(f"{a.name} at {a.position}")

print("=== SIMULATION END ===")
