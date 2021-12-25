import numpy as np
import time

from diffusion import evolve


grid_shape = (512, 512)


def run_experiment(num_iterations):
    scratch = np.zeros(grid_shape, dtype=np.double, order='F')
    grid = np.zeros(grid_shape, dtype=np.double, order='F')

    start = time.time()
    for i in range(num_iterations):
        evolve(grid, scratch, 1.0, 0.1)
        grid, scratch = scratch, grid
    return time.time() - start


if __name__ == "__main__":
    print(f"diffusion took {run_experiment(500)} seconds")
    # diffusion took 0.12355899810791016 seconds