from algorithms.prioritized_astar import prioritized_astar
from map import GridMap
from agent import Agent


def main():
    print("=== SIMULATION START ===")

    # Grid size
    width = 6
    height = 6

    # Obstacles
    obstacles = [
        (1, 2), (2, 2), (3, 2),
        (3, 3), (3, 4)
    ]

    # Create grid
    grid = GridMap(width, height, obstacles)

    # Goal position
    goal = (5, 5)

    # Agents (id, start_x, start_y, speed)
    agents = [
        Agent("LAND 1", 0, 0, speed=1),
        Agent("LAND 2", 0, 5, speed=1),
        Agent("LAND 3", 5, 0, speed=1)
    ]

    # Collect start positions
    starts = [(a.x, a.y) for a in agents]

    # Run prioritized A*
    paths = prioritized_astar(grid, starts, goal)

    # Assign paths to agents
    for agent, path in zip(agents, paths):
        agent.path = path
        if path:
            print(f"{agent.name} path: {path}")
        else:
            print(f"{agent.name} -> NO PATH FOUND")

    print("\nFINAL MAP VIEW (TEXT):")
    grid.render(agents, goal)

    print("\nOPENING GUI...")
    grid.render_gui(agents, goal)

    print("=== SIMULATION END ===")


if __name__ == "__main__":
    main()
