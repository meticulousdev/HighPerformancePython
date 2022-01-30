import math
import timeit
from multiprocessing import Pool
import create_range


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
    to_i = 21
    if not check_prime_in_range((n, (from_i, to_i))):
        return False
    
    from_i = to_i
    to_i = int(math.sqrt(n)) + 1

    ranges_to_check = create_range.create(from_i, to_i, nbr_processes)
    ranges_to_check = list(zip(len(ranges_to_check) * [n], ranges_to_check))

    assert len(ranges_to_check) == nbr_processes

    results = pool.map(check_prime_in_range, ranges_to_check)
    if False in results:
        return False
    return True


if __name__ == "__main__":
    NBR_PROCESSES = 4
    pool = Pool(processes=NBR_PROCESSES)
    print("Testing with {} processes".format(NBR_PROCESSES))
    for label, nbr in [("trivial non-prime", 112272535095295),
                       ("expensive non-prime18_1", 100109100129100369),
                       ("expensive non-prime18_2", 100109100129101027),
                       ("prime18_1", 100109100129100151),
                       ("prime18_2", 100109100129162907)]:
        time_costs = timeit.repeat(stmt="check_prime({}, pool, {})".format(nbr, NBR_PROCESSES), repeat=20, number=1,
                                   setup="from __main__ import pool, check_prime")
        print("{:19} ({}) {: 3.6f}s".format(label, nbr, min(time_costs)))

# Testing with 4 processes
# trivial non-prime   (112272535095295)  0.000002s
# expensive non-prime18_1 (100109100129100369)  2.968264s
# expensive non-prime18_2 (100109100129101027)  3.475149s
# prime18_1           (100109100129100151)  3.978340s
# prime18_2           (100109100129162907)  4.303354s
