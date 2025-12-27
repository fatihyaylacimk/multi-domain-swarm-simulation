from agents.agent import Agent
from agents.air_agent import AirAgent
from environment.map import GridMap
from algorithms.bfs import bfs
from simulation.scenario import load_scenario


if __name__ == "__main__":
    # Senaryoyu yükle
    scenario = load_scenario()

    # Haritayı oluştur
    grid = GridMap(
        width=scenario["map"]["width"],
        height=scenario["map"]["height"]
    )

    for obs in scenario["map"]["obstacles"]:
        grid.add_obstacle(obs[0], obs[1])

    goal = scenario["goal"]

    # LAND swarm
    land_agents = [
        Agent(1, "LAND", 0, 0, 1),
        Agent(2, "LAND", 0, 1, 1),
        Agent(3, "LAND", 1, 0, 1),
    ]

    # AIR agent
    air_agent = AirAgent(4, 0, 4, 2)

    occupied = set()

    print("=== SIMULATION START ===")

    # LAND agentlar BFS ile gider
    for agent in land_agents:
        path = bfs(grid, agent.position(), goal)
        print(f"\nLAND {agent.agent_id} path:", path)

        for step in path[1:]:
            dx = step[0] - agent.x
            dy = step[1] - agent.y
            next_pos = (agent.x + dx, agent.y + dy)

            if next_pos in occupied:
                print(f"LAND {agent.agent_id} blocked at", next_pos)
                break

            moved = agent.move(dx, dy, grid)
            if not moved:
                break

            occupied.add(agent.position())

        print(f"LAND {agent.agent_id} final:", agent.position())

    # AIR agent direkt hedefe gider
    air_agent.move(goal[0] - air_agent.x, goal[1] - air_agent.y, grid)
    print("\nAIR final:", air_agent.position())

    # FINAL HARİTA GÖRÜNÜMÜ
    print("\nFINAL MAP VIEW:")
    grid.render(agents=land_agents + [air_agent], goal=goal)

    print("=== SIMULATION END ===")
