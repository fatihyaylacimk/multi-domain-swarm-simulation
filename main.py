from agents.agent import Agent
from environment.map import GridMap

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

    print("Start:", agent1.position())

    moved = agent1.move(1, 0, grid)
    print("Move right:", moved, "Position:", agent1.position())

    moved = agent1.move(1, 0, grid)
    print("Move right:", moved, "Position:", agent1.position())

    moved = agent1.move(0, 1, grid)
    print("Move down:", moved, "Position:", agent1.position())

