import numpy as np
import randomwalk3d as rw

def plot_walks():

    N = 100

    rw3d1 = rw.RandomWalk3D()
    rw3d1.generate(N, step=rw.Step.cartesian, crossing=False)
    rw3d1.plot()

    rw3d2 = rw.RandomWalk3D()
    rw3d2.generate(N, step=rw.Step.spherical1, crossing=False)
    rw3d2.plot()

def bias_study():

    N = 5000

    rw.Step.scatter_steps(N, step=rw.Step.spherical2)

def main():

    bias_study()

if __name__ == "__main__":
    main()