import time
import math


# prime number
def check_prime(number):
    sqrt_number = math.sqrt(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number / i).is_integer():
            return False


# TODO Chapter 06 ?
def check_prime_invalid(number):
    sqrt_number = math.sqrt(number)
    numbers = range(2, int(sqrt_number) + 1)
    for i in range(0, len(numbers), 5):
        # invalid code
        result = (number / numbers[i:(i + 5)]).is_integer()
        if any(result):
            return  False
    return True


# python virtual machine
def search_fast(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
    return False


def search_slow(haystack, needle):
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value


def search_unknown1(haystack, needle):
    return any((item == needle for item in haystack))


def search_unknown2(haystack, needle):
    return any([item == needle for item in haystack])


if __name__ == "__main__":
    time1 = time.time()
    print(f"check_prime(10,000,000) = {check_prime(10_000_000)}")
    time2 = time.time()
    print(f"elapsed time: {time2 - time1}")

    print(f"check_prime(10,000,019) = {check_prime(10_000_019)}")
    time3 = time.time()
    print(f"elapsed time: {time3 - time2}")
