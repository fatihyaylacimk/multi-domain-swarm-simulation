# ===============================
# MULTI-DOMAIN SWARM SIMULATION
# MAIN ENTRY FILE
# ===============================

from environment.map import GridMap
from agents.agent import Agent
from algorithms.prioritized_astar import prioritized_astar


def main():
    print("=== SIMULATION START ===")

    # -------------------------------
    # GRID CONFIGURATION
    # -------------------------------
    width = 10
    height = 10

    obstacles = [
        # örnek engeller (istersen ekleyebilirsin)
        # (3, 3), (3, 4), (3, 5)
    ]

    grid = GridMap(width, height, obstacles)

    # -------------------------------
    # AGENTS
    # name, x, y, speed
    # -------------------------------
    agents = [
        Agent("LAND 1", 0, 0, speed=1),
        Agent("LAND 2", 2, 2, speed=1),
        Agent("LAND 3", 4, 4, speed=1),
    ]

    # -------------------------------
    # GOAL
    # -------------------------------
    goal = (5, 5)

    # -------------------------------
    # PATH PLANNING
    # -------------------------------
    paths = prioritized_astar(grid, agents, goal)

    # -------------------------------
    # OUTPUT RESULTS
    # -------------------------------
    for agent in agents:
        name = agent.name
        path = paths.get(name, [])

        if not path:
            print(f"{name} -> NO PATH FOUND")
            print(f"{name} path: []")
            print(f"{name} final: NO MOVE")
        else:
            print(f"{name} path: {path}")
            print(f"{name} final: {path[-1]}")

    # -------------------------------
    # VISUALIZATION (GUI)
    # -------------------------------
    print("\nFINAL MAP VIEW:")
    grid.render_gui(agents, goal)

    print("=== SIMULATION END ===")


# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    main()
