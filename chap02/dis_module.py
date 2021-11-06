import time
from functools import wraps

import dis
import julia_set


def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time


# @timefn
def fn_expressive(upper=1_000_000):
    total = 0
    for n in range(upper):
        total += n
    return total


# @timefn
def fn_terse(upper=1_000_000):
    return sum(range(upper))


if __name__ == '__main__':
    # dis.dis(julia_set.calculate_z_serial_purepython)
    assert fn_expressive() == fn_terse(), "Expect identical results from both functions"

    print("fn_expressive")
    dis.dis(fn_expressive)

    print("fn_terse")
    dis.dis(fn_terse)
