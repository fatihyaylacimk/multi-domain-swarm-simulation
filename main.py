
  from agents.agent import Agent
from agents.air_agent import AirAgent
from environment.map import GridMap
from algorithms.bfs import bfs

if __name__ == "__main__":
    grid = GridMap(width=5, height=5)
    grid.add_obstacle(2, 2)

    # LAND swarm
    land_agents = [
        Agent(1, "LAND", 0, 0, 1),
        Agent(2, "LAND", 0, 1, 1),
        Agent(3, "LAND", 1, 0, 1),
    ]

    # AIR agent
    air_agent = AirAgent(4, 0, 4, 2)

    goal = (4, 4)

    # LAND agents BFS ile gider
    for agent in land_agents:
        path = bfs(grid, agent.position(), goal)
        print(f"LAND {agent.agent_id} path:", path)

        for step in path[1:]:
            dx = step[0] - agent.x
            dy = step[1] - agent.y
            agent.move(dx, dy, grid)

        print(f"LAND {agent.agent_id} final:", agent.position())

    # AIR agent direkt gider
    air_agent.move(goal[0] - air_agent.x, goal[1] - air_agent.y, grid)
    print("AIR final:", air_agent.position())
