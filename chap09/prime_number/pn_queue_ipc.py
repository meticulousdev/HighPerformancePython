import argparse
import math
from multiprocessing import Manager, Pool, Process
import time


FLAG_ALL_DONE = b"WORK_FINISHED"
FLAG_WORKER_FINISHED_PROCESSING = b"WORKER_FINISHED_PROCESSING"


def check_prime(possible_primes_queue, definite_primes_queue):
    while True:
        n = possible_primes_queue.get()
        if n == FLAG_ALL_DONE:
            definite_primes_queue.put(FLAG_WORKER_FINISHED_PROCESSING)
            break
        else:
            if n % 2 == 0:
                continue
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    break
            else:
                definite_primes_queue.put(n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Project description")
    parser.add_argument("nbr_workers", type=int, help="Number of workers e.g. 1, 2, 4, 8")
    args = parser.parse_args("2")

    print(args)

    primes = []

    # multiprocessing.Manager()
    manager = Manager()
    possible_primes_queue = manager.Queue()
    definite_primes_queue = manager.Queue()

    pool = Pool(processes=args.nbr_workers)
    processes = []
    for _ in range(args.nbr_workers):
        # multiprocessing.Process()
        p = Process(target=check_prime, args=(possible_primes_queue, definite_primes_queue))
        processes.append(p)
        p.start()
    
    t1 = time.time()
    number_range = range(100_000_000, 101_000_000)

    for possible_prime in number_range:
        possible_primes_queue.put(possible_prime)
    print("ALL JOBS ADDED TO THE QUEUE")
    
    for n in range(args.nbr_workers):
        possible_primes_queue.put(FLAG_ALL_DONE)
    
    print("NOW WAITING FOR RESULTS...")
    processors_indicating_they_have_finished = 0
    while True:
        new_result = definite_primes_queue.get()
        if new_result == FLAG_WORKER_FINISHED_PROCESSING:
            print(f"WORKER {processors_indicating_they_have_finished} HAS JUST FINISHED")
            processors_indicating_they_have_finished += 1
            if processors_indicating_they_have_finished == args.nbr_workers:
                break
        else:
            primes.append(new_result)
    assert processors_indicating_they_have_finished == args.nbr_workers

    print(f"Took: {time.time() - t1}")
    print(len(primes), primes[:10], primes[-10:])

    # Namespace(nbr_workers=1)
    # ALL JOBS ADDED TO THE QUEUE
    # NOW WAITING FOR RESULTS...
    # WORKER 0 HAS JUST FINISHED
    # Took: 38.75331997871399
    # 54208 [100000007, 100000037, 100000039, 100000049, 100000073, 100000081, 100000123, 100000127, 100000193, 100000213] 
    # [100999889, 100999897, 100999901, 100999903, 100999919, 100999939, 100999949, 100999979, 100999981, 100999993]

    # Namespace(nbr_workers=2)
    # ALL JOBS ADDED TO THE QUEUE
    # NOW WAITING FOR RESULTS...
    # WORKER 0 HAS JUST FINISHED
    # WORKER 1 HAS JUST FINISHED
    # Took: 34.6600182056427
    # 54208 [100000007, 100000037, 100000039, 100000049, 100000073, 100000081, 100000123, 100000127, 100000193, 100000213] 
    # [100999889, 100999897, 100999901, 100999903, 100999919, 100999939, 100999949, 100999979, 100999981, 100999993]

    # Namespace(nbr_workers=4)
    # ALL JOBS ADDED TO THE QUEUE
    # NOW WAITING FOR RESULTS...
    # WORKER 0 HAS JUST FINISHED
    # WORKER 1 HAS JUST FINISHED
    # WORKER 2 HAS JUST FINISHED
    # WORKER 3 HAS JUST FINISHED
    # Took: 36.96143984794617
    # 54208 [100000007, 100000037, 100000039, 100000049, 100000073, 100000081, 100000123, 100000127, 100000193, 100000213] 
    # [100999889, 100999897, 100999901, 100999903, 100999919, 100999939, 100999949, 100999979, 100999981, 100999993]

    # Namespace(nbr_workers=8)
    # ALL JOBS ADDED TO THE QUEUE
    # NOW WAITING FOR RESULTS...
    # WORKER 0 HAS JUST FINISHED
    # WORKER 1 HAS JUST FINISHED
    # WORKER 2 HAS JUST FINISHED
    # WORKER 3 HAS JUST FINISHED
    # WORKER 4 HAS JUST FINISHED
    # WORKER 5 HAS JUST FINISHED
    # WORKER 6 HAS JUST FINISHED
    # WORKER 7 HAS JUST FINISHED
    # Took: 36.826987981796265
    # 54208 [100000007, 100000037, 100000039, 100000049, 100000073, 100000081, 100000123, 100000127, 100000193, 100000213] 
    # [100999889, 100999897, 100999901, 100999903, 100999919, 100999939, 100999949, 100999979, 100999981, 100999993]