from distutils.core import setup 
from distutils.extension import Extension
import numpy as np

# clang error unsupported option '-fopenmp' 
# reference: https://githubmemory.com/repo/mmolero/pypoisson/issues/3?page=2

# env: Macbook AIR M1 - MacOS Monterey Version 12.0.1

import os
os.environ["CC"] = "/opt/homebrew/opt/llvm/bin/clang"
os.environ["CXX"] = "/opt/homebrew/opt/llvm/bin/clang++"

# ext_modules = [Extension("cythonfn_OpenMP",
#                          ["cythonfn_OpenMP.pyx"],
#                          extra_compile_args=['-fopenmp'],
#                          extra_link_args=['-fopenmp'])]

ext_modules = [Extension("cythonfn_OpenMP",
                         ["cythonfn_OpenMP.pyx"],
                         langauge="c++",
                         extra_compile_args=['-w', '-fopenmp', '-stdlib=libc++'],
                         extra_link_args=['-fopenmp', '-stdlib=libc++'])]

from Cython.Build import cythonize
setup(ext_modules=cythonize(ext_modules, 
                            compiler_directives={'language_level': "3"}),
      include_dirs=[np.get_include()])
