import matplotlib.pyplot as plt
import time

# ======================
# GRID AYARLARI
# ======================
GRID_SIZE = 6

# ======================
# AGENT SINIFI
# ======================
class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.path = [(x, y)]

    def move(self):
        if self.x < GRID_SIZE - 1:
            self.x += 1
        elif self.y < GRID_SIZE - 1:
            self.y += 1
        self.path.append((self.x, self.y))


# ======================
# GRAFIK ÇIZIMI
# ======================
def render(agent):
    plt.clf()

    # grid
    plt.xticks(range(GRID_SIZE))
    plt.yticks(range(GRID_SIZE))
    plt.grid(True)

    # agent path
    xs = [p[0] for p in agent.path]
    ys = [p[1] for p in agent.path]
    plt.plot(xs, ys, marker="o")

    # agent current position
    plt.scatter(agent.x, agent.y, s=200)

    plt.xlim(-0.5, GRID_SIZE - 0.5)
    plt.ylim(-0.5, GRID_SIZE - 0.5)
    plt.title("Agent Movement")
    plt.pause(0.3)


# ======================
# MAIN
# ======================
def main():
    plt.ion()
    agent = Agent()

    for _ in range(10):
        agent.move()
        render(agent)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
