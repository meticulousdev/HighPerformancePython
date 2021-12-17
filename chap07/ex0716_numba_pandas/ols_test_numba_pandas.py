import time
import numpy as np
import pandas as pd
from numba import jit


def ols_lstsq_raw(row):
    X = np.arange(row.shape[0])
    ones = np.ones(row.shape[0])
    A = np.vstack((X, ones)).T
    m, c = np.linalg.lstsq(A, row, rcond=-1)[0]
    return m


def test_data(ncol: int, nrow: int):
    np.random.seed(1)
    data = np.zeros((nrow, ncol))
    for i in range(data.shape[0]):
        data[i, :] = np.random.random(ncol) + 1

    df = pd.DataFrame(data)
    # print(df.head())
    # print(df.info())
    # print(df.describe())
    return df


if __name__ == '__main__':
    ncol = 14 
    nrow = 100_000
    df = test_data(ncol, nrow)

    start = time.time()
    results = df.apply(ols_lstsq_raw, axis=1, raw=True)
    print(f"elapsed time: {time.time() - start}")
    # elapsed time: 4.4591920375823975
    
    start = time.time()
    ols_lstsq_raw_values_numba = jit(ols_lstsq_raw, nopython=True)
    results = df.apply(ols_lstsq_raw_values_numba, axis=1, raw=True)
    print(f"elapsed time: {time.time() - start}")
    # elapsed time: 3.2230031490325928

    start = time.time()
    results = df.apply(ols_lstsq_raw_values_numba, axis=1, raw=True)
    print(f"elapsed time: {time.time() - start}")
    # elapsed time: 0.5738708972930908
