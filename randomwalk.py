import numpy as np
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(999999999)

class RandomWalk():

    def __init__(self, dim):

        self.dim = dim
        self.path = [tuple([0] * self.dim)]

    def get_next(self):
        dir = np.random.randint(0, self.dim-1)
        next = list(self.path[-1])
        next[dir] = next[dir] + int(np.random.choice([-1, 1]))
        return tuple(next)
    
    def gc(self, N):
        for i in range(N):
            self.path.append(self.get_next())

    def distance(self):
        return np.linalg.norm(self.path[-1])

def main():

    Ns = []
    for i in range(100):
        Ns.append(10 * (i + 1))
    dists = []
    measures = 100

    for N in Ns:
        print(N)
        dist_list = []
        for i in range(measures):
            rw = RandomWalk(2)
            rw.gc(N)
            dist_list.append(rw.distance())
        dists.append(np.mean(dist_list))

    plt.plot(Ns, dists)
    plt.show()

if __name__ == "__main__":
    main()
