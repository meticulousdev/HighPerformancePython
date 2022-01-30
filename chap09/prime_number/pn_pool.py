import math
import time
import multiprocessing
#import numpy as np
import itertools


def check_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    primes = []
    NBR_PROCESSES = 4
    pool = multiprocessing.Pool(processes=NBR_PROCESSES)

    t1 = time.time()
    number_range = range(100_000_000, 101_000_000)  # C
    
    are_primes = pool.map(check_prime, number_range)
    primes = [p for p in itertools.compress(number_range, are_primes)]

    print(f"Took: {time.time() - t1}")
    print(len(primes), primes[:10], primes[-10:])

    # Took: 2.890532970428467
    # 54208 [100000007, 100000037, 100000039, 100000049, 100000073, 100000081, 100000123, 100000127, 100000193, 100000213] 
    # [100999889, 100999897, 100999901, 100999903, 100999919, 100999939, 100999949, 100999979, 100999981, 100999993]
