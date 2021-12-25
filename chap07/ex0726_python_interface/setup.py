"""
setup.py for cpython diffusion module. The extention can be built by running

    $ python setup.py build_ext --inplace

which will create __cdiffusion.so__ file, which can be directly imported into Python
"""

from distutils.core import setup, Extension
from numpy.distutils.misc_util import get_numpy_include_dirs

__version__ = "0.1"


cdiffusion = Extension('cdiffusion',
                       sources=['cdiffusion.c', 'python_interface.c'],
                       extra_compile_args=['-O3', '-std=c11', '-Wall', '-p', '-pg'],
                       extra_link_args=['-lc'])

setup(name='diffusion',
      version=__version__,
      ext_modules=[cdiffusion],
      packages=['diffusion'],
      include_dirs=get_numpy_include_dirs())
