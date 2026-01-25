import numpy as np
import matplotlib.pyplot as plt
import randomwalk3d as rw
import random as r

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

            print(int(dist))

        return dists, walk_data, error_data
    
    def acceptance_rate(runs=100, max_dist=100, step=rw.Step.cartesian, crossing=True, last=True, min_angle=0):
        
        acceptance_rates = []
        dists = np.linspace(1, max_dist, max_dist)

        for dist in dists:

            accepted_walks = 0

            for i in range(runs):

                walk = rw.RandomWalk()
                walk.generate(int(dist), step, crossing=crossing, last=last, min_angle=min_angle)

                if walk.unique_nodes():

                    accepted_walks += 1

            print(int(dist), accepted_walks)

            acceptance_rates.append(accepted_walks / runs)

        return dists, acceptance_rates
    
    def depth_gnc(max_dist):

        walk = rw.RandomWalk()
        depth_data = walk.generate(max_dist, step=rw.Step.cartesian, crossing=False)
        itters = np.linspace(1, len(depth_data), len(depth_data))

        return itters, depth_data

    def scatter_steps(runs=100, step=rw.Step.cartesian):

        points = np.array(step())
        for i in range(runs-1):
            points = np.vstack((points, np.array(step())))

        return points

class Cartesian():

    def result_gcwalk():

        dists, walk_data, error_data = GetResult.walks(runs=1000, max_dist=100, step=rw.Step.cartesian)

        plt.errorbar(dists, walk_data, error_data, color="black", ecolor="red", capsize=2, elinewidth=1)

        plt.grid()
        plt.xlabel("Walk Length")
        plt.ylabel("Average Distance")
        plt.show()

    def results_walks():

        dists_gc, walk_data_gc, error_data_gc = GetResult.walks(runs=1000, max_dist=100, step=rw.Step.cartesian)
        dists_gnl, walk_data_gnl, error_data_gnl = GetResult.walks(runs=1000, max_dist=100, step=rw.Step.cartesian, last=False)
        dists_gnc, walk_data_gnc, error_data_gnc = GetResult.walks(runs=1000, max_dist=100, step=rw.Step.cartesian, crossing=False)

        plt.errorbar(dists_gc, walk_data_gc, error_data_gc, color="black", ecolor="red", capsize=2, elinewidth=1, label="No step restriction")
        plt.errorbar(dists_gnl, walk_data_gnl, error_data_gnl, color="grey", ecolor="red", capsize=2, elinewidth=1, label="Avoid previous node")
        plt.errorbar(dists_gnc, walk_data_gnc, error_data_gnc, color="gainsboro", ecolor="red", capsize=2, elinewidth=1, label="Avoid all previous nodes")
        
        plt.grid()
        plt.legend()
        plt.xlabel("Walk Length")
        plt.ylabel("Average Distance")
        plt.show()

    def acceptance_rate():

        dists_gc, acceptance_rate_gc = GetResult.acceptance_rate(runs=1000, max_dist=50, step=rw.Step.cartesian)
        dists_gnl, acceptance_rate_gnl = GetResult.acceptance_rate(runs=1000, max_dist=50, step=rw.Step.cartesian, last=False)

        plt.plot(dists_gc, acceptance_rate_gc, color="black", label="No step restriction")
        plt.plot(dists_gnl, acceptance_rate_gnl, color="grey", label="Avoid previous node")

        plt.grid()
        plt.legend()
        plt.xlabel("Walk Length")
        plt.ylabel("Acceptance Rate")
        plt.show()

    def depth_gnc():

        itters1, depth_data1 = GetResult.depth_gnc(100)
        itters2, depth_data2 = GetResult.depth_gnc(100)
        itters3, depth_data3 = GetResult.depth_gnc(100)
        itters4, depth_data4 = GetResult.depth_gnc(100)
        itters5, depth_data5 = GetResult.depth_gnc(100)
        
        plt.plot(itters1, depth_data1, color="black")
        plt.plot(itters2, depth_data2, color="dimgrey")
        plt.plot(itters3, depth_data3, color="darkgrey")
        plt.plot(itters4, depth_data4, color="silver")
        plt.plot(itters5, depth_data5, color="gainsboro")

        plt.grid()
        plt.xlabel("Itterations")
        plt.ylabel("Depth")
        plt.show()

        # Do how many itterations it takes compared to length??

def main():

    Cartesian.depth_gnc()

if __name__ == "__main__":
    main()