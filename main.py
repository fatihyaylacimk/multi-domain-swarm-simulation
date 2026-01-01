import matplotlib.pyplot as plt
import time

# ======================
# GRID AYARLARI
# ======================
GRID_SIZE = 6

# ENGELLER (x, y)
OBSTACLES = [(2, 2), (2, 3), (3, 3), (4, 1)]

# ======================
# AGENT SINIFI
# ======================
class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.path = [(x, y)]

    def can_move(self, x, y):
        if x < 0 or y < 0 or x >= GRID_SIZE or y >= GRID_SIZE:
            return False
        if (x, y) in OBSTACLES:
            return False
        return True

    def move(self):
        # önce sağa dene
        if self.can_move(self.x + 1, self.y):
            self.x += 1
        # sağ olmazsa yukarı dene
        elif self.can_move(self.x, self.y + 1):
            self.y += 1
        else:
            print("NO MOVE")
            return

        self.path.append((self.x, self.y))


# ======================
# GRAFIK
# ======================
def render(agent):
    plt.clf()

    plt.xticks(range(GRID_SIZE))
    plt.yticks(range(GRID_SIZE))
    plt.grid(True)

    # ENGELLER
    for ox, oy in OBSTACLES:
        plt.scatter(ox, oy, c="red", s=400, marker="s")

    # AGENT YOLU
    xs = [p[0] for p in agent.path]
    ys = [p[1] for p in agent.path]
    plt.plot(xs, ys, marker="o")

    # AGENT
    plt.scatter(agent.x, agent.y, c="blue", s=200)

    plt.xlim(-0.5, GRID_SIZE - 0.5)
    plt.ylim(-0.5, GRID_SIZE - 0.5)
    plt.title("Agent with Obstacles")

    plt.pause(0.4)


# ======================
# MAIN
# ======================
def main():
    plt.ion()
    agent = Agent()

    for _ in range(20):
        agent.move()
        render(agent)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
input("Press ENTER to exit...")

