import time
from joblib import Parallel, delayed

from pi_estimation import estimate_nbr_points_in_quarter_circle


if __name__ == "__main__":
    nbr_samples_in_total = 1e8
    nbr_parrallel_blocks = 4
    nbr_samples_per_worker = nbr_samples_in_total / nbr_parrallel_blocks

    t1 = time.time()
    nbr_in_quater_unit_circles = Parallel(n_jobs=nbr_parrallel_blocks, verbose=1) \
        (delayed(estimate_nbr_points_in_quarter_circle)(nbr_samples_per_worker) \
            for sameple_idx in range(nbr_parrallel_blocks))
    t2 = time.time()
    pi_estimate = sum(nbr_in_quater_unit_circles) * 4 / float(nbr_samples_in_total)
    print(f"elapsed time: {t2 - t1}")
    print(f"pi estimate : {pi_estimate}")

    # [Parallel(n_jobs=4)]: Using backend LokyBackend with 4 concurrent workers.
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 4082
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 4081
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 4084
    # Executing estiate_nbr_points_in_quater_circle             with 25,000,000.0, on pid 4083
    # [Parallel(n_jobs=4)]: Done   2 out of   4 | elapsed:   10.1s remaining:   10.1s
    # [Parallel(n_jobs=4)]: Done   4 out of   4 | elapsed:   10.1s finished
    # elapsed time: 10.083842039108276
    # pi estimate : 3.14167388 

    # [Parallel(n_jobs=8)]: Using backend LokyBackend with 8 concurrent workers.
    # Executing estiate_nbr_points_in_quater_circle             with 12,500,000.0, on pid 4219
    # Executing estiate_nbr_points_in_quater_circle             with 12,500,000.0, on pid 4217
    # Executing estiate_nbr_points_in_quater_circle             with 12,500,000.0, on pid 4220
    # Executing estiate_nbr_points_in_quater_circle             with 12,500,000.0, on pid 4218
    # Executing estiate_nbr_points_in_quater_circle             with 12,500,000.0, on pid 4221
    # Executing estiate_nbr_points_in_quater_circle             with 12,500,000.0, on pid 4222
    # Executing estiate_nbr_points_in_quater_circle             with 12,500,000.0, on pid 4224
    # Executing estiate_nbr_points_in_quater_circle             with 12,500,000.0, on pid 4223
    # [Parallel(n_jobs=8)]: Done   2 out of   8 | elapsed:    7.2s remaining:   21.7s
    # [Parallel(n_jobs=8)]: Done   8 out of   8 | elapsed:    7.5s finished
    # elapsed time: 7.398721694946289
    # pi estimate : 3.14186832
