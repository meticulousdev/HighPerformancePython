from cffi import FFI
import numpy as np
import time

grid_shape = (512, 512)

ffi = FFI()
ffi.cdef("void evolve(double **in, double **out, double D, double dt);")
lib = ffi.verify(
r"""
void evolve(double in[][512], double out[][512], double D, double dt)
{
    int i, j;
    double laplacian;
    for(i = 1; i < 511; i++)
    {
        for(j = 1; j < 511; j++)
        {
            laplacian = in[i+1][j] + in[i-1][j] + in[i][j+1] + in[i][j-1] - 4 * in[i][j];
            out[i][j] = in[i][j] + D * dt * laplacian;
        }
    }
}
""", extra_compile_args=["-O3"]
)


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
    # diffusion took 0.05594968795776367 seconds
    # warning: incompatible pointer types passing 'double **' 
    # to parameter of type 'double (*)[512]' [-Wincompatible-pointer-types]
    # 2 warnings generated.