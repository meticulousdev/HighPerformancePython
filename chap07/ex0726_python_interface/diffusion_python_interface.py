import numpy as np
import time
from cdiffusion import evolve


grid_shape = (512, 512)


def run_experiment(num_iterations):
    next_grid = np.zeros(grid_shape)
    grid = np.zeros(grid_shape)

    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    grid[block_low:block_high, block_low:block_high] = 0.005

    start = time.time()
    for i in range(num_iterations):
        evolve(grid, next_grid, 0.1)
        grid, next_grid = next_grid, grid
    return time.time() - start


if __name__ == "__main__":
    print(f"diffusion took {run_experiment(500)} seconds")
    # diffusion took 0.05146193504333496 seconds
