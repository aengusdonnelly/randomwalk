import numpy as np
import matplotlib.pyplot as plt
import randomwalk3d as rw

class Data:
    
    def  __init__(self):
        self.data = []

    def add(self, data):
        self.data.append(data)

    def remove(self, index):
        self.data.pop(index)

    def mean(self):
        return sum(self.data)/len(self.data)
    
    def SE(self):

        N = len(self.data)
        x_bar = self.mean()

        sum = 0

        for data in self.data:

            sum += (data - self.mean()) ** 2

        return np.sqrt((1 / (N * (N - 1))) * sum)

class GetResult:

    def walks(runs=100, max_dist=100, step=rw.Step.cartesian, crossing=True, last=True, min_angle=0):

        walk_data = []
        error_data = []

        dists = np.linspace(1, max_dist, max_dist)

        for dist in dists:

            walk_dists = Data()

            for i in range(runs):

                walk = rw.RandomWalk()
                walk.generate(int(dist), step, crossing=crossing, last=last, min_angle=min_angle)
                walk_dists.add(walk.distance())

            walk_data.append(walk_dists.mean())
            error_data.append(walk_dists.SE())

        return dists, walk_data, error_data

    def scatter_steps(runs=100, step=rw.Step.cartesian):

        points = np.array(step())
        for i in range(runs-1):
            points = np.vstack((points, np.array(step())))

        return points

def main():

    dists, walk_data, error_data = GetResult.walks(runs=100, max_dist=100, step=rw.Step.spherical1, last=False, min_angle=np.pi/2)
    plt.errorbar(dists, walk_data, error_data, color="black", ecolor="red", capsize=2, elinewidth=1)
    plt.show()

if __name__ == "__main__":
    main()