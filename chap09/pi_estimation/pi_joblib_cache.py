import time
import os
import random
from joblib import Parallel, delayed, Memory


memory = Memory("./joblib_cache", verbose=0)

@memory.cache
def estimate_nbr_points_in_quarter_circle_with_idx(nbr_estimates, idx):
    print(f"Executing estimate_nbr_points_in_quater_circle with \
            {nbr_estimates} on sample {idx} on pid {os.getpid()}")
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
    nbr_parrallel_blocks = 4
    nbr_samples_per_worker = nbr_samples_in_total / nbr_parrallel_blocks

    t1 = time.time()
    nbr_in_quater_unit_circles = Parallel(n_jobs=nbr_parrallel_blocks, verbose=1) \
        (delayed(estimate_nbr_points_in_quarter_circle_with_idx) \
        (nbr_samples_per_worker, idx) for idx in range(nbr_parrallel_blocks))
    t2 = time.time()
    pi_estimate = sum(nbr_in_quater_unit_circles) * 4 / float(nbr_samples_in_total)
    print(f"elapsed time: {t2 - t1}")
    print(f"pi estimate : {pi_estimate}")

    # first run
    # [Parallel(n_jobs=4)]: Using backend LokyBackend with 4 concurrent workers.
    # Executing estimate_nbr_points_in_quater_circle with             25000000.0 on sample 0 on pid 6182
    # Executing estimate_nbr_points_in_quater_circle with             25000000.0 on sample 1 on pid 6184
    # Executing estimate_nbr_points_in_quater_circle with             25000000.0 on sample 2 on pid 6183
    # Executing estimate_nbr_points_in_quater_circle with             25000000.0 on sample 3 on pid 6185
    # [Parallel(n_jobs=4)]: Done   2 out of   4 | elapsed:   10.2s remaining:   10.2s
    # [Parallel(n_jobs=4)]: Done   4 out of   4 | elapsed:   10.3s finished
    # elapsed time: 10.26299786567688
    # pi estimate : 3.14143392

    # second run
    # [Parallel(n_jobs=4)]: Using backend LokyBackend with 4 concurrent workers.
    # [Parallel(n_jobs=4)]: Done   2 out of   4 | elapsed:    0.6s remaining:    0.6s
    # [Parallel(n_jobs=4)]: Done   4 out of   4 | elapsed:    0.6s finished
    # elapsed time: 0.58650803565979
    # pi estimate : 3.14143392
