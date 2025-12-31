import numpy as np
import matplotlib.pyplot as plt

class RandomWalk3D():

    def __init__(self):

        self.path = [(0, 0, 0)]

    def generate(self, N, coordinates="cartesian", crossing=True):

        if crossing:
            self.gc(N, coordinates=coordinates)
        else:
            self.gnc(N, coordinates=coordinates)


    def step(self, coordinates="cartesian"):

        if coordinates == "cartesian":

            n = int(np.random.rand() * 6)

            if n == 0: dx, dy, dz = 1, 0, 0
            elif n == 1: dx, dy, dz = 0, 1, 0
            elif n == 2: dx, dy, dz = 0, 0, 1
            elif n == 3: dx, dy, dz = -1, 0, 0
            elif n == 4: dx, dy, dz = 0, -1, 0
            else: dx, dy, dz = 0, 0, -1
        
        elif coordinates == "spherical":

            phi = np.random.uniform(0, 2*np.pi)
            theta = np.random.uniform(0, np.pi)

            dx = np.sin(theta) * np.cos(phi)
            dy = np.sin(theta) * np.sin(phi)
            dz = np.cos(theta)

        return dx, dy, dz

    def gc(self, N, coordinates="cartesian"):

        for i in range(N):
            dx, dy, dz = self.step(coordinates=coordinates)
            next = (self.path[-1][0] + dx, self.path[-1][1] + dy, self.path[-1][2] + dz)
            
            self.path.append(next)

    def gnc(self, N, coordinates="cartesian"):

        if N == 0:
            return True
        
        c = self.path[-1]

        while True:

            dx, dy, dz = self.step(coordinates=coordinates)
            next = (self.path[-1][0] + dx, self.path[-1][1] + dy, self.path[-1][2] + dz)
            
            if next in self.path:
                continue

            else:
                self.path.append(next)

                if self.gnc(N-1, coordinates=coordinates):
                    return True
                else:
                    self.path.pop(-1)
        
    def distance(self):
        return np.sqrt((self.path[0][0] - self.path[-1][0]) ** 2 + (self.path[0][1] - self.path[-1][1]) ** 2 + (self.path[0][2] - self.path[-1][2]) ** 2)

    def plot(self, points=True):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])
        ax.scatter(self.path[0][0], self.path[0][1], self.path[0][2], color="red", s=50, label="Starting point")
        
        for i in range(1, len(self.path)):
            p = self.path[i-1]
            c = self.path[i]

            ax.plot3D([p[0], c[0]], [p[1], c[1]], [p[2], c[2]], color="black")
            
            if points:
                ax.scatter(self.path[i][0], self.path[i][1], self.path[i][2], color="black", s=20)

        plt.legend()
        plt.title("3D random walk of length "+str(len(self.path)-1))
        plt.show()

def main():

    N = 100

    rw3d1 = RandomWalk3D()
    rw3d1.generate(N, coordinates="cartesian", crossing=False)
    rw3d1.plot()

    rw3d2 = RandomWalk3D()
    rw3d2.generate(N, coordinates="spherical", crossing=False)
    rw3d2.plot()

if __name__ == "__main__":
    main()