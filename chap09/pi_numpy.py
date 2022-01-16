import os
import random

import numpy as np

import time


def estimate_nbr_points_in_quarter_circle(nbr_samples):
    np.random.seed()
    xs = np.random.uniform(0, 1, int(nbr_samples))
    ys = np.random.uniform(0, 1, int(nbr_samples))
    estimate_inside_quarter_unit_circle = (xs * xs + ys * ys) <= 1
    nbr_trials_in_quarter_unit_circle = np.sum(estimate_inside_quarter_unit_circle)
    return nbr_trials_in_quarter_unit_circle


if __name__ == "__main__":
    nbr_samples_in_total = 1e8
    t1 = time.time()
    nbr_in_quater_unit_circles = estimate_nbr_points_in_quarter_circle(nbr_samples_in_total)
    t2 = time.time()
    print("numpy")
    print(f"elapsed time: {t2 - t1}")
    pi_estimate = nbr_in_quater_unit_circles * 4 / nbr_samples_in_total
    print(f"pi estimate : {pi_estimate}")
    
    # numpy
    # elapsed time: 1.356821060180664
    # pi estimate : 3.14200604