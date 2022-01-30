from concurrent.futures import process
import math
from multiprocessing import Pool


def check_prime_in_range(n_from_i_to_i):
    (n, (from_i, to_i)) = n_from_i_to_i
    if n % 2 == 0:
        return False
    assert from_i % 2 != 0
    for i in range(from_i, int(to_i), 2):
        if n % i == 0:
            return False
    return True


def check_prime(n, pool, nbr_processes):
    from_i = 3
    to_i = math.sqrt(n) + 1

    ranges_to_check = create_range.create(from_i, to_i, nbr_processes)
    ranges_to_check = zip(len(ranges_to_check) * [n], ranges_to_check)

    assert len(ranges_to_check) == nbr_processes

    results = pool.map(check_prime_in_range, ranges_to_check)
    if False in results:
        return False
    return True


# 343p
if __name__ == "__main__":
    # print(check_prime_in_range((101, (3, 99))))
    NBR_PROCESSES = 4
    pool = Pool(processes=NBR_PROCESSES)