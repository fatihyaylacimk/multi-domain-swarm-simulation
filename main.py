from map import GridMap
from algorithms.prioritized_astar import prioritized_astar

def main():
    print("=== SIMULATION START ===")

    # Grid ayarları
    width = 10
    height = 10

    obstacles = [
        (2, 2), (2, 3), (2, 4),
        (4, 6), (5, 6), (6, 6)
    ]

    grid = GridMap(width, height, obstacles)

    # Hedef
    goal = (5, 5)

    # Agent başlangıç noktaları
    agents = [
        {"name": "LAND 1", "start": (0, 0)},
        {"name": "LAND 2", "start": (1, 8)},
        {"name": "LAND 3", "start": (8, 1)},
    ]

    all_paths = []

    for agent in agents:
        path = prioritized_astar(
            grid=grid,
            start=agent["start"],
            goal=goal,
            reserved_paths=all_paths
        )

        if path:
            print(f"{agent['name']} path: {path}")
            print(f"{agent['name']} final: {path[-1]}")
            all_paths.append(path)
        else:
            print(f"{agent['name']} -> NO PATH FOUND")
            print(f"{agent['name']} final: NO MOVE")
            all_paths.append([])

    print("\nFINAL MAP VIEW:")
    grid.render(
        agents=[type("A", (), {"x": p[-1][0], "y": p[-1][1]})
                for p in all_paths if p],
        goal=goal
    )

    print("=== SIMULATION END ===")

    # >>> GUI AÇILAN KISIM (ÖNEMLİ) <<<
    print("GUI OPENING...")
    grid.render_gui(
        agents=[type("A", (), {"x": p[-1][0], "y": p[-1][1]})
                for p in all_paths if p],
        goal=goal
    )


if __name__ == "__main__":
    main()
