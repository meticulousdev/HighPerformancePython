from cffi import FFI

ffi = FFI()
ffi.cdef(
r"""
    struct Point 
    {
        double x;
        double y;
        ...;
    };
    struct Point do_calculation();
"""
)
lib = ffi.verify(
r"""
    #include "complicated.h"
"""
)