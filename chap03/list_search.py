import time
from functools import wraps

import bisect
import random


def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time


@timefn
def linear_search(needle, array):
    for i, item in enumerate(array):
        if item == needle:
            return i
    return -1


@timefn
def binary_search(needle, haystack):
    imin, imax = 0, len(haystack)
    while True:
        if imin > imax:
            return -1
        midpoint = (imin + imax) // 2

        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] < needle:
            imin = midpoint + 1
        else:
            return midpoint


def find_closest(haystack, needle):
    i = bisect.bisect_left(haystack, needle)
    if i == len(haystack):
        return i - 1
    elif haystack[i] == needle:
        return i
    elif i > 0:
        j = i - 1
        if haystack[i] - needle > needle - haystack[j]:
            return j
    return i


if __name__ == "__main__":
    list_data = [9, 18, 18, 18, 19, 29, 42, 56, 61, 88, 95]
    target = 61

    print(f"{linear_search(target, list_data)}")
    print(f"{binary_search(target, list_data)}")

    important_numbers = []
    for i in range(10):
        new_number = random.randint(0, 1000)
        bisect.insort(important_numbers, new_number)
    print(important_numbers)

    closest_index = find_closest(important_numbers, -250)
    print(f"Closest value to -250: {important_numbers[closest_index]}")
    
    closest_index = find_closest(important_numbers, 500)
    print(f"Closest value to 500: {important_numbers[closest_index]}")
    
    closest_index = find_closest(important_numbers, 1100)
    print(f"Closest value to 1100: {important_numbers[closest_index]}")
