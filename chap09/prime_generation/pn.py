import math
import time


def check_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    primes = []
    t1 = time.time()
    number_range = range(100_000_000, 101_000_000)

    for possible_prime in number_range:
        if check_prime(possible_prime):
            primes.append(possible_prime)

    print("Took:", time.time() - t1)
    print(len(primes), primes[:10], primes[-10:])

    # Took: 10.941862106323242
    # 54208 [100000007, 100000037, 100000039, 100000049, 100000073, 100000081, 100000123, 100000127, 100000193, 100000213] 
    # [100999889, 100999897, 100999901, 100999903, 100999919, 100999939, 100999949, 100999979, 100999981, 100999993]