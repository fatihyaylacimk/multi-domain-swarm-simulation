    occupied = set()  # dolu hücreler

    for agent in land_agents:
        path = bfs(grid, agent.position(), goal)
        print(f"LAND {agent.agent_id} path:", path)

        for step in path[1:]:
            dx = step[0] - agent.x
            dy = step[1] - agent.y
            next_pos = (agent.x + dx, agent.y + dy)

            if next_pos in occupied:
                print(f"LAND {agent.agent_id} blocked by another agent at", next_pos)
                break

            moved = agent.move(dx, dy, grid)
            if not moved:
                break

            occupied.add(agent.position())

        print(f"LAND {agent.agent_id} final:", agent.position())
