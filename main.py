from environment.map import GridMap
from agents.agent import Agent
import time
import os

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

# HIZ TANIMI
SPEED = {
    "LAND": 1,
    "AIR": 2
}

for a in agents:
    if a.type == "AIR":
        a.plan(grid, set())

print("=== SIMULATION START ===")

while True:
    os.system("cls")
    active = False

    # LAND konumları AIR için engel
    forbidden = set(a.position for a in agents if a.type=="LAND")

    for a in agents:
        if a.type == "AIR" and not a.finished:
            a.plan(grid, forbidden)

    # 🔥 HIZ FARKI BURADA
    for a in agents:
        for _ in range(SPEED[a.type]):
            a.move()

        if not a.finished:
            active = True

    # ÇİZİM
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
