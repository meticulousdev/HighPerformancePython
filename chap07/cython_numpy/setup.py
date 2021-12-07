from distutils.core import setup 
from Cython.Build import cythonize
import numpy as np


# numpy/arrayobject.h' file not found
# setup(ext_modules=cythonize('cythonfn_numpy.pyx', compiler_directives={'language_level': "3"}))

# warning: tp_print
# python version error?
setup(ext_modules=cythonize('cythonfn_numpy.pyx', compiler_directives={'language_level': "3"}),
      include_dirs=[np.get_include()])
