from collections import deque

def bfs(grid, start, goal):
    queue = deque([start])
    visited = {start: None}

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < grid.width and 0 <= ny < grid.height:
                if grid.is_free(nx, ny) and (nx, ny) not in visited:
                    visited[(nx, ny)] = (x, y)
                    queue.append((nx, ny))

    if goal not in visited:
        return []

    # yolu geri sar
    path = []
    current = goal
    while current:
        path.append(current)
        current = visited[current]

    path.reverse()
    return path
