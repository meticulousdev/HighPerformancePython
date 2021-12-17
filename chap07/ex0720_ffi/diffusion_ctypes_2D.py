import ctypes
import numpy as np
import time

grid_shape = (512, 512)
_diffusion = ctypes.CDLL("diffusion.so")

TYPE_INT = ctypes.c_int
TYPE_DOUBLE = ctypes.c_double
TYPE_DOUBLE_SS = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))

_diffusion.evolve.argtypes = [TYPE_DOUBLE_SS, TYPE_DOUBLE_SS, TYPE_DOUBLE, TYPE_DOUBLE]
_diffusion.evolve.restype = None


def evolve(grid, out, dt, D=1.0):
    assert grid.shape == (512, 512)    
    cdt = TYPE_DOUBLE(dt)
    cD = TYPE_DOUBLE(D)
    pointer_grid = grid.ctypes.data_as(TYPE_DOUBLE_SS)
    pointer_out = out.ctypes.data_as(TYPE_DOUBLE_SS)

    _diffusion.evolve(pointer_grid, pointer_out, cD, cdt)


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
    # diffusion took 0.05464816093444824 seconds
