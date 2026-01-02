def air_path(start, goal):
    x, y = start
    gx, gy = goal
    path = []

    while x != gx or y != gy:
        if x < gx:
            x += 1
        elif x > gx:
            x -= 1

        if y < gy:
            y += 1
        elif y > gy:
            y -= 1

        path.append((x, y))

    return path
