import math
import timeit
from multiprocessing import Pool
import create_range
import mmap


SERIAL_CHECK_CUTOFF = 21
CHECK_EVERY = 1000
FLAG_CLEAR = 0
FLAG_SET = 1
print("CHECK_EVERY", CHECK_EVERY)

sh_mem = mmap.mmap(-1, 1)


def check_prime_in_range(n_from_i_to_i):
    (n, (from_i, to_i)) = n_from_i_to_i
    if n % 2 == 0:
        return False
    assert from_i % 2 != 0
    check_every = CHECK_EVERY
    for i in range(from_i, int(to_i), 2):
        check_every -= 1
        if not check_every:
            sh_mem.seek(0)
            flag = sh_mem.read_byte()
            if flag == FLAG_SET:
                return False
            check_every = CHECK_EVERY

        if n % i == 0:
            sh_mem.seek(0)
            sh_mem.write_byte(FLAG_SET)
            return False
    return True


def check_prime(n, pool, nbr_processes):
    from_i = 3
    to_i = SERIAL_CHECK_CUTOFF
    sh_mem.seek(0)
    sh_mem.write_byte(FLAG_CLEAR)
    if not check_prime_in_range((n, (from_i, to_i))):
        return False
    sh_mem.seek(0)
    sh_mem.write_byte(FLAG_CLEAR)

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

# CHECK_EVERY 1000
# Testing with 4 processes
# trivial non-prime   (112272535095295)  0.000003s
# CHECK_EVERY 1000
# CHECK_EVERY 1000
# CHECK_EVERY 1000
# CHECK_EVERY 1000
# expensive non-prime18_1 (100109100129100369)  5.154643s
# expensive non-prime18_2 (100109100129101027)  5.081381s
# prime18_1           (100109100129100151)  5.078885s
# prime18_2           (100109100129162907)  4.802648s
