f2py -c -m diffusion --fcompiler=gfortran --opt='-O3' diffusion.f90

warning: "Using deprecated NumPy API, disable it with "          
"#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]

>>> diffusion?
  File "<stdin>", line 1
    diffusion?
             ^
SyntaxError: invalid syntax

>>> help(diffusion)
Help on module diffusion:

NAME
    diffusion

DESCRIPTION
    This module 'diffusion' is auto-generated with f2py (version:1.20.3).
    Functions:
      evolve(grid,next_grid,d,dt)
    .

DATA
    __f2py_numpy_version__ = '1.20.3'
    evolve = <fortran object>

VERSION
    1.20.3

FILE
    /Users/.../diffusion.cpython-39-darwin.so