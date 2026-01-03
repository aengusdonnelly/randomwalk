import randomwalk3d as rw

def plot_walks():
    N = 100

    rw3d1 = rw.RandomWalk3D()
    rw3d1.generate(N, step=rw.Step.cartesian, crossing=False)
    rw3d1.plot()

    rw3d2 = rw.RandomWalk3D()
    rw3d2.generate(N, step=rw.Step.spherical1, crossing=False)
    rw3d2.plot()

def main():
    plot_walks()

if __name__ == "__main__":
    main()