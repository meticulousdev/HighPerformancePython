from distutils.core import setup 
from Cython.Build import cythonize


setup(ext_modules=cythonize('cythonfn_cdef_abs_boundscheck.pyx', compiler_directives={'language_level': "3"}))
