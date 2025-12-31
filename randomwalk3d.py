import numpy as np
import matplotlib.pyplot as plt

class Step():

    def cartesian():

        n = int(np.random.rand() * 6)

        if n == 0: dx, dy, dz = 1, 0, 0
        elif n == 1: dx, dy, dz = 0, 1, 0
        elif n == 2: dx, dy, dz = 0, 0, 1
        elif n == 3: dx, dy, dz = -1, 0, 0
        elif n == 4: dx, dy, dz = 0, -1, 0
        else: dx, dy, dz = 0, 0, -1

        return dx, dy, dz

    def spherical1():

        phi = np.random.uniform(0, 2*np.pi)
        theta = np.random.uniform(0, np.pi)

        dx = np.sin(theta) * np.cos(phi)
        dy = np.sin(theta) * np.sin(phi)
        dz = np.cos(theta)

        return dx, dy, dz
    
    def scatter_steps(N, step_opt=spherical1):

        points = []
        for i in range(N):
            points.append(Step.step_opt())

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])
        ax.scatter(points, color="red", s=10, label="Starting point")

class RandomWalk3D():

    def __init__(self):

        self.path = [(0, 0, 0)]

    def gc(self, N, step_opt=Step.cartesian):

        for i in range(N):
            dx, dy, dz = step_opt()
            next = (self.path[-1][0] + dx,
                    self.path[-1][1] + dy,
                    self.path[-1][2] + dz)
            
            self.path.append(next)

    def gnc(self, N, step_opt=Step.cartesian):

        if N == 0:
            return True
        
        c = self.path[-1]

        while True:

            dx, dy, dz = step_opt()
            next = (self.path[-1][0] + dx,
                    self.path[-1][1] + dy,
                    self.path[-1][2] + dz)
            
            if next in self.path:
                continue

            else:
                self.path.append(next)

                if self.gnc(N-1, step_opt=step_opt):
                    return True
                else:
                    self.path.pop(-1)
        
    def distance(self):

        return np.sqrt((self.path[0][0] - self.path[-1][0]) ** 2 +
                       (self.path[0][1] - self.path[-1][1]) ** 2 +
                       (self.path[0][2] - self.path[-1][2]) ** 2)
    
    def generate(self, N, step_opt=Step.cartesian, crossing=True):

        if crossing:
            self.gc(N, step_opt=step_opt)
        else:
            self.gnc(N, step_opt=step_opt)

    def plot(self, points=True):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])
        ax.scatter(self.path[0][0], self.path[0][1], self.path[0][2],
                   color="red", s=50, label="Starting point")
        
        for i in range(1, len(self.path)):
            p = self.path[i-1]
            c = self.path[i]

            ax.plot3D([p[0], c[0]], [p[1], c[1]], [p[2], c[2]], color="black")
            
            if points:
                ax.scatter(self.path[i][0], self.path[i][1],
                           self.path[i][2], color="black", s=20)

        plt.legend()
        plt.title("3D random walk of length "+str(len(self.path)-1))
        plt.show()