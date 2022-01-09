import os
import random

import time

from multiprocessing import Pool

from pi_estimation import estimate_nbr_points_in_quarter_circle


if __name__ == "__main__":
    nbr_samples_in_total = 1e8
    print("w/ multiprocessing")
    nbr_parrallel_blocks = 4
    pool = Pool(processes=nbr_parrallel_blocks)
    nbr_samples_per_worker = nbr_samples_in_total / nbr_parrallel_blocks
    print(f"Making {nbr_samples_per_worker:,} samples per {nbr_parrallel_blocks} worker")

    nbr_trials_per_process = [nbr_samples_per_worker] * nbr_parrallel_blocks 
    t1 = time.time()
    nbr_in_quater_unit_circles = pool.map(estimate_nbr_points_in_quarter_circle, nbr_trials_per_process)
    t2 = time.time()
    pi_estimate = sum(nbr_in_quater_unit_circles) * 4 / float(nbr_samples_in_total)
    print(f"elapsed time: {t2 - t1}")
    print(f"pi estimate : {pi_estimate}")

    # w/ multiprocessing
    # Making 25,000,000.0 samples per 4 worker
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 2530
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 2531
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 2532
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 2533
    # elapsed time: 9.693703889846802
    # pi estimate : 3.14121164
