from itertools import count, groupby, filterfalse, islice


def itertools_yield():
    yield 0
    yield 1
    yield 2


def itertools_yield_test():
    itertools_yield()
    print(itertools_yield)
    print(dir(itertools_yield))

    for i in itertools_yield():
        print(i)


def itertools_count_test():
    print("count test")
    print("print(cnt)")
    cnt = count()
    print(dir(cnt))
    for _ in range(5):
        print(cnt)

    print("print(cnt.__next__())")
    for _ in range(5):
        print(cnt.__next__())

    print("for i in count(): print(i)")
    for i in count():
        print(i) 
        if i > 5:
            break


if __name__ == "__main__":
    print("main")
    # itertools_yield_test()
    # itertools_count_test()
