from agents.agent import Agent
from agents.air_agent import AirAgent
from environment.map import GridMap
from algorithms.bfs import bfs

if __name__ == "__main__":
    grid = GridMap(width=5, height=5)
    grid.add_obstacle(2, 2)

    land_agent = Agent(
        agent_id=1,
        agent_type="LAND",
        x=0,
        y=0,
        speed=1
    )

    air_agent = AirAgent(
        agent_id=2,
        x=0,
        y=4,
        speed=2
    )

    goal = (4, 4)

    # LAND agent BFS ile gider
    path = bfs(grid, land_agent.position(), goal)
    print("LAND path:", path)

    for step in path[1:]:
        dx = step[0] - land_agent.x
        dy = step[1] - land_agent.y
        land_agent.move(dx, dy, grid)
        print("LAND moved to:", land_agent.position())

    # AIR agent direkt gider
    air_agent.move(goal[0] - air_agent.x, goal[1] - air_agent.y, grid)
    print("AIR moved to:", air_agent.position())
