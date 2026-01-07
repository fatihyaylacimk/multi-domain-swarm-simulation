from environment.map import GridMap
from agents.agent import Agent
import time, os

GRID = 10

grid = GridMap(
    GRID, GRID,
    obstacles={(4,4),(4,5),(5,4)}
)

agents = [
    Agent("LAND 1",(0,0),(5,5),"LAND"),
    Agent("LAND 2",(1,0),(1,5),"LAND"),
    Agent("AIR 1",(9,0),(0,9),"AIR"),
    Agent("AIR 2",(9,9),(0,0),"AIR"),
]

SPEED = {"LAND":1, "AIR":2}

print("=== SIMULATION START ===")

while True:
    os.system("cls")
    active = False

    land_positions = set(a.position for a in agents if a.type=="LAND")

    # AIR yeniden planlar
    for a in agents:
        if a.type=="AIR" and not a.finished:
            a.plan(grid, land_positions)

    # 🔮 AIR FUTURE COLLISION CHECK
    air_future = {}
    for a in agents:
        if a.type=="AIR" and not a.finished:
            air_future[a.name] = a.predict_next_positions(SPEED["AIR"])

    # Çakışan AIR kareleri
    blocked_air = set()
    for name1, f1 in air_future.items():
        for name2, f2 in air_future.items():
            if name1 != name2:
                blocked_air |= set(f1) & set(f2)

    # Hareket
    for a in agents:
        for _ in range(SPEED[a.type]):
            blocked = land_positions | blocked_air
            a.move(blocked)
        if not a.finished:
            active = True

    # Çizim
    board = [["." for _ in range(GRID)] for _ in range(GRID)]
    for o in grid.obstacles:
        board[o[1]][o[0]] = "#"

    for a in agents:
        x,y = a.position
        board[y][x] = "A" if a.type=="AIR" else "L"

    for r in board:
        print(" ".join(r))

    if not active:
        break

    time.sleep(0.5)

print("=== SIMULATION END ===")
