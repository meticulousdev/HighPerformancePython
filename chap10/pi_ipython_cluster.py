import time
import ipyparallel as ipp
from ipyparallel import require


@require('random')
def estimate_nbr_points_in_quarter_circle(nbr_estimates):
    print(f"Executing estimate_nbr_points_in_quarter_circlewith {nbr_estimates:,} on pid {os.getpid()}")   
    nbr_trials_in_quarter_unit_circle = 0
    for step in range(int(nbr_estimates)):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        is_in_unit_circle = x * x + y * y <= 1.0
        nbr_trials_in_quarter_unit_circle += is_in_unit_circle
    return nbr_trials_in_quarter_unit_circle


if __name__ == "__main__":
    c = ipp.Client()
    nbr_engines = len(c.ids)
    print("We're using {} engines".format(nbr_engines))
    nbr_samples_in_total = 1e8
    nbr_parallel_blocks = 4

    dview = c[:]

    nbr_samples_per_worker = nbr_samples_in_total / nbr_parallel_blocks
    t1 = time.time()
    nbr_in_quarter_unit_circles = dview.apply_sync(estimate_nbr_points_in_quarter_circle, \
                                                   nbr_samples_per_worker)
    print("Estimates made:", nbr_in_quarter_unit_circles)

    nbr_jobs = len(nbr_in_quarter_unit_circles)
    pi_estimate = sum(nbr_in_quarter_unit_circles) * 4 / nbr_samples_in_total
    print("Estimated pi", pi_estimate)
    print("Delta:", time.time() - t1)

# In [1]: import ipyparallel as ipp

# In [2]: c = ipp.Client()

# In [3]: dview = c[:]

# In [4]: with dview.sync_imports():
#    ...:     import os
# importing os on engine(s)

# In [5]: %run pi_ipython_cluster.py
# We're using 4 engines
# Estimates made: [19632349, 19635686, 19637861, 19638363]
# Estimated pi 3.14177036
# Delta: 9.572163820266724