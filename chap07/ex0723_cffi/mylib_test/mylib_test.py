from cffi import FFI

ffi = FFI()
ffi.set_source('mylib', 
r"""
#include <stdio.h>
int a = 1;
""")
ffi.cdef(r"""
void puts(const char *);
int a = 1;
""")
ffi.compile(verbose=True)

import mylib
mylib.lib.puts(b"Hello World!")
print(mylib.lib.a)