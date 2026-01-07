import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal, forbidden):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for n in grid.neighbors(current):
            if n in forbidden:
                continue

            temp = g[current] + 1
            if n not in g or temp < g[n]:
                g[n] = temp
                f = temp + heuristic(n, goal)
                heapq.heappush(open_set, (f, n))
                came_from[n] = current

    return []
