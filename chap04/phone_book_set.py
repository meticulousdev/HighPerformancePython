from typing import List, Set

import time
from functools import wraps


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
def list_unique_names(phonebook):
    unique_names: List = []
    for name, phonenumber in phonebook:
        first_name, last_name = name.split(" ", 1)
        for unique in unique_names:
            if unique == first_name:
                break
        else:
            unique_names.append(first_name)
    return len(unique_names)


@timefn
def set_unique_names(phonebook):
    unique_names: Set = set()
    for name, phonenumber in phonebook:
        first_name, last_name = name.split(" ", 1)
        unique_names.add(first_name)
    return len(unique_names)


if __name__ == "__main__":
    phonebook: List = [
        ("John Doe", "555-555-5555"),
        ("Albert Einstein", "212-555-5555"),
        ("John Murphey", "202-555-5555"),
        ("Albert Rutherford", "647-555-5555"),
        ("Guido van Rossum", "301-555-5555")
    ]

    print(f"Number of unique names from set method: {set_unique_names(phonebook)}")
    print(f"Number of unique names from list method: {list_unique_names(phonebook)}")