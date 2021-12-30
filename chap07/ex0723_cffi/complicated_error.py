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
    struct Point pnt;
"""
)

# lib = ffi.verify(
# r"""
#     #include "complicated.h"
# """
# )

lib = ffi.verify(
r"""
#include <stdbool.h>

struct Point
{
    double x;
    double y;
    bool isActive;
    const char *id;
    int num_times_visited;
};
"""
)