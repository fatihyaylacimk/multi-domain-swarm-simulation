from agents.agent import Agent
from environment.map import GridMap
from algorithms.bfs import bfs

if __name__ == "__main__":
    grid = GridMap(width=5, height=5)
    grid.add_obstacle(2, 2)

    agent1 = Agent(
        agent_id=1,
        agent_type="LAND",
        x=0,
        y=0,
        speed=1
    )

    start = agent1.position()
    goal = (4, 4)

    path = bfs(grid, start, goal)
    print("Path:", path)

    for step in path[1:]:
        dx = step[0] - agent1.x
        dy = step[1] - agent1.y
        agent1.move(dx, dy, grid)
        print("Moved to:", agent1.position())
