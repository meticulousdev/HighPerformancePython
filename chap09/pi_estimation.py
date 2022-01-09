import os
import random

import time


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
    t1 = time.time()
    nbr_in_quater_unit_circles = estimate_nbr_points_in_quarter_circle(nbr_samples_in_total)
    t2 = time.time()
    print("w/o multiprocessing")
    print(f"elapsed time: {t2 - t1}")
    pi_estimate = nbr_in_quater_unit_circles * 4 / nbr_samples_in_total
    print(f"pi estimate : {pi_estimate}")

    # w/o multiprocessing
    # Executing estiate_nbr_points_in_quater_circle             with 100,000,000.0, on pid 2122
    # elapsed time: 34.236793994903564
    # pi estimate: 3.14173576
