import numpy as np
import randomwalk3d as rw

def plot_walks():

    N = 3

    rw3d1 = rw.RandomWalk3D()
    rw3d1.generate(N, step=rw.Step.spherical2, last=False, min_angle=(3/4)*np.pi)
    rw3d1.plot()

def bias_study():

    N = 100

    rw.Step.scatter_steps(N, step=rw.Step.spherical2)

def main():

    plot_walks()
    #bias_study()

if __name__ == "__main__":
    main()