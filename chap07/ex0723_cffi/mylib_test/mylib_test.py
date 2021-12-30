from cffi import FFI

ffi = FFI()
ffi.set_source('mylib', r"""#include <stdio.h>""")
ffi.cdef(r"""void puts(const char *);""")
ffi.compile(verbose=True)

import mylib
mylib.lib.puts(b"Hello World!")