from typing import List, Dict

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


def find_phonenumber(phonebook, name):
    for n, p in phonebook:
        if n == name:
            return p
    return None


@timefn
def find_phonenumber_list(phonebook: List):
    print(f"John Doe's phone number is {find_phonenumber(phonebook, 'John Doe')}")


@timefn
def find_phonenumber_dict(phonebook: Dict):
    print(f"John Doe's phone number is {phonebook['John Doe']}")


# cPfrofile: Too fast to calculate elapsed time
if __name__ == "__main__":
    phonebook: List = [
        ("John Doe", "555-555-5555"),
        ("Albert Einstein", "212-555-555")
    ]

    print(f"John Doe's phone number is {find_phonenumber(phonebook, 'John Doe')}")
    find_phonenumber_list(phonebook)

    phonebook: Dict = {
        "John Doe": "555-555-5555",
        "Albert Einstein": "212-555-555"
    }

    print(f"John Doe's phone number is {phonebook['John Doe']}")
    find_phonenumber_dict(phonebook)
