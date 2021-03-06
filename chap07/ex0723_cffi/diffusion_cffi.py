from cffi import FFI
import numpy as np
import time

grid_shape = (512, 512)

ffi = FFI()
ffi.cdef("void evolve(double **in, double **out, double D, double dt);")
# open vscode ex0723_cffi
lib = ffi.dlopen("../ex0721_ffi_ctypes/diffusion.so")


def evolve(grid, out, dt, D=1.0):
    pointer_grid = ffi.cast("double**", grid.ctypes.data)
    pointer_out = ffi.cast("double**", out.ctypes.data)
    lib.evolve(pointer_grid, pointer_out, D, dt)


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
    # diffusion took 0.05642199516296387 seconds
