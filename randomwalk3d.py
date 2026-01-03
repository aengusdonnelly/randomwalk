import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

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
    
    def spherical2():
        
        while True:
            x = np.random.uniform(-1, 1)
            y = np.random.uniform(-1, 1)
            z = np.random.uniform(-1, 1)

            norm = np.linalg.norm(np.array((x, y, z)))

            if norm > 1:
                continue
            else:
                break

        dx = x / norm
        dy = y / norm
        dz = z / norm
        return dx, dy, dz

    def scatter_steps(N, step=spherical1):

        points = np.array(step())
        for i in range(N-1):
            points = np.vstack((points, np.array(step())))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

        ax.scatter(points[:,0], points[:,1], points[:,2],
                   color="red", s=1, label="Starting point")

        ax.set_box_aspect((1, 1 ,1))
        plt.show()

        span = np.linspace(-1, 1, 500)

        plt.plot(span, scs.gaussian_kde(points[:,0])(span),
                 color="blue", linewidth=2, label="x values")
        plt.plot(span, scs.gaussian_kde(points[:,1])(span),
                 color="red", linewidth=2, label="y values")
        plt.plot(span, scs.gaussian_kde(points[:,2])(span),
                 color="black", linewidth=2, label="z values")
        
        plt.hist(points[:,0], bins=100, density=True,color="blue", alpha=0.5)
        plt.hist(points[:,1], bins=100, density=True, color="red", alpha=0.5)
        plt.hist(points[:,2], bins=100, density=True, color="black", alpha=0.5)

        plt.legend()
        plt.xlabel("Position")
        plt.ylabel("Density")
        plt.show()

class RandomWalk3D():

    def __init__(self):

        self.path = [(0, 0, 0)]

    def gc(self, N, step=Step.cartesian):

        for i in range(N):
            dx, dy, dz = step()
            next = (self.path[-1][0] + dx,
                    self.path[-1][1] + dy,
                    self.path[-1][2] + dz)
            
            self.path.append(next)

    def gnc(self, N, step=Step.cartesian):

        if N == 0:
            return True
        
        c = self.path[-1]

        while True:

            dx, dy, dz = step()
            next = (self.path[-1][0] + dx,
                    self.path[-1][1] + dy,
                    self.path[-1][2] + dz)
            
            if next in self.path:
                continue

            else:
                self.path.append(next)

                if self.gnc(N-1, step=step):
                    return True
                else:
                    self.path.pop(-1)
        
    def distance(self):

        return np.sqrt((self.path[0][0] - self.path[-1][0]) ** 2 +
                       (self.path[0][1] - self.path[-1][1]) ** 2 +
                       (self.path[0][2] - self.path[-1][2]) ** 2)
    
    def generate(self, N, step=Step.cartesian, crossing=True):

        if crossing:
            self.gc(N, step=step)
        else:
            self.gnc(N, step=step)

    def plot(self, points=True):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

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
        ax.set_box_aspect((1, 1 ,1))
        plt.show()