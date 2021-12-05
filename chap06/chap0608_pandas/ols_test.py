import time
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from line_profiler import LineProfiler

def ols_sklearn(row):
    est = LinearRegression()
    X = np.arange(row.shape[0]).reshape(-1, 1)
    est.fit(X, row.values)
    m = est.coef_[0]
    return m


def ols_sklearn_lineprofiler(row) -> None:
    est = LinearRegression()
    X = np.arange(row.shape[0]).reshape(-1, 1)

    print("Run on a single row")
    # TODO: name 'est' is not defined 
    # lp = LineProfiler(est.fit)
    # lp.run("est.fit(X, row.values)")
    # lp.print_stats()

    # ref.: https://stackoverflow.com/questions/23885147/how-do-i-use-line-profiler-from-robert-kern
    lp = LineProfiler()
    lp_wrapper = lp(est.fit)
    lp_wrapper(X, row.values)
    lp.print_stats()


def ols_lstsq(row):
    X = np.arange(row.shape[0])
    ones = np.ones(row.shape[0])
    A = np.vstack((X, ones)).T
    m, c = np.linalg.lstsq(A, row.values, rcond=-1)[0]
    return m


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
    # # example 6-24
    # ncol = 14
    # nrow = 3
    # df = test_data(ncol, nrow)
    # 
    # m = ols_sklearn(df.iloc[0])
    # print(m)
    # 
    # # example 6-25
    # ols_sklearn_lineprofiler(df.iloc[0])
    # 
    # m = ols_lstsq(df.iloc[0])
    # print(m)
    # 
    # m = ols_lstsq_raw(df.iloc[0].to_numpy())
    # print(m)

    # example 6-26 ~ 6-29
    ncol = 14 
    nrow = 100_000
    df = test_data(ncol, nrow)
    
    start = time.time()
    ms = []
    for row_idx in range(df.shape[0]):
        row = df.iloc[row_idx]
        m = ols_lstsq(row)
        ms.append(m)
    results = pd.Series(ms)
    print(f"elapsed time: {time.time() - start}")
    # elapsed time: 14.74239706993103

    start = time.time()
    ms = []
    for row_idx, row in df.iterrows():
        m = ols_lstsq(row)
        ms.append(m)
    results = pd.Series(ms)
    print(f"elapsed time: {time.time() - start}")
    # elapsed time: 11.308629989624023

    start = time.time()
    ms = df.apply(ols_lstsq, axis=1)
    results = pd.Series(ms)
    print(f"elapsed time: {time.time() - start}")
    # elapsed time: 5.7157301902771

    start = time.time()
    ms = df.apply(ols_lstsq_raw, axis=1, raw=True)
    results = pd.Series(ms)
    print(f"elapsed time: {time.time() - start}")
    # elapsed time: 3.817999839782715
