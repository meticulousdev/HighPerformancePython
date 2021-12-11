from distutils.core import setup 
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np


# numpy/arrayobject.h' file not found
# setup(ext_modules=cythonize('cythonfn_numpy.pyx', compiler_directives={'language_level': "3"}))

# warning: tp_print
# python version error?
# setup(ext_modules=cythonize('cythonfn_numpy.pyx', compiler_directives={'language_level': "3"}),
#       include_dirs=[np.get_include()])

# solution:
# TODO: extra_compile_args and extra_link_args
ext_modules = [Extension("cythonfn_numpy",
                         ["cythonfn_numpy.pyx"],
                         langauge="c++",
                         extra_compile_args=['-w', '-stdlib=libc++'],
                         extra_link_args=['-stdlib=libc++'])]

setup(ext_modules=cythonize(ext_modules, 
                            compiler_directives={'language_level': "3"}),
      include_dirs=[np.get_include()])
