import os
import random

import time

from multiprocessing import Pool


def estimate_nbr_points_in_quarter_circle(nbr_estimates):
    print(f"Executing estiate_nbr_points_in_quater_circle \
            with {nbr_estimates:,}, on pid {os.getpid()}")
    nbr_trials_in_quarter_unit_circle = 0
    for _ in range(int(nbr_estimates)):
    # for step in range(int(nbr_estimates)):
        # step?
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        is_in_unit_circle = x * x + y * y <= 1.0
        nbr_trials_in_quarter_unit_circle += is_in_unit_circle

    return nbr_trials_in_quarter_unit_circle


if __name__ == "__main__":
    nbr_samples_in_total = 1e8
    
    # w/o multiprocessing 
    t1 = time.time()
    nbr_in_quater_unit_circles = estimate_nbr_points_in_quarter_circle(nbr_samples_in_total)
    t2 = time.time()
    print("w/o multiprocessing")
    print(f"elapsed time: {t2 - t1}")
    pi_estimate = nbr_in_quater_unit_circles * 4 / nbr_samples_in_total
    print(f"pi estimate : {pi_estimate}")

    # w/o multiprocessing
    # Executing estiate_nbr_points_in_quater_circle             with 100,000,000.0, on pid 2122
    # elapsed time: 173.42957472801208
    # pi estimate: 3.14173576

    # w/ multiprocessing
    print("w/ multiprocessing")
    nbr_parrallel_blocks = 4
    pool = Pool(processes=nbr_parrallel_blocks)
    nbr_samples_per_worker = nbr_samples_in_total / nbr_parrallel_blocks
    print(f"Making {nbr_samples_per_worker:,} samples per {nbr_parrallel_blocks} worker")

    nbr_trials_per_process = [nbr_samples_per_worker] * nbr_parrallel_blocks 
    t1 = time.time()
    nbr_in_quater_unit_circles = pool.map(estimate_nbr_points_in_quarter_circle, nbr_trials_per_process)
    t2 = time.time()
    pi_estimate = sum(nbr_trials_per_process) * 4 / float(nbr_samples_in_total)
    print(f"elapsed time: {t2 - t1}")
    print(f"pi estimate : {pi_estimate}")

    # w/ multiprocessing
    # Making 25,000,000.0 samples per 4 worker
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 2530
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 2531
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 2532
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 2533
    # elapsed time: 51.123993158340454
    # pi estimate : 4.0
