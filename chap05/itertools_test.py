from itertools import count, groupby, filterfalse, islice
import operator
from typing import List, Dict, Tuple

# itertools_yield
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
# end of itertools_yield_test


# itertools_count
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
# end of itertools_count_test


# itertools_filterfalse
def check_one(value):
    # print(f"check_one value: {value}")
    if value == 1:
        return True
    return False


def itertools_filterfalse_test():
    data_list: List = [0, 2, 1, 6, 1, 1, 4]
    for i in filterfalse(check_one, data_list):
        print(i)
# end of itertools_filterfalse_test


# itertools_groupby
def itertools_groupby_test():
    data_dict: Dict = {'a': 1, 'b': 2, 'c': 3}
    for k, d in groupby(data_dict):
        print(f"{k}, {list(d)}")
    print()

    data_list: List = ['a', 'b', 'c', 'a', 'b']
    for k, d in groupby(data_list):
        print(f"{k}, {list(d)}")
    print()

    # wikidocs
    data_ld: List[Dict] = [{'key': 'a', 'value': 1},
                           {'key': 'b', 'value': 2},
                           {'key': 'c', 'value': 3},
                           {'key': 'd', 'value': 4},
                           {'key': 'c', 'value': 3},
                           {'key': 'd', 'value': 4}]

    for k, d in groupby(data_ld, key=operator.itemgetter('key')):
        print(f"{k}, {list(d)[0]['value']}")
    print()

    # stack overflow
    data_lt: List[Tuple] = [("animal", "dog"), 
                            ("animal", "cat"), 
                            ("plant", "flower"), 
                            ("plant", "tree"), 
                            ("human", "male"),
                            ("human", "female")] 

    for key, group in groupby(data_lt, lambda x: x[0]):
        for thing in group:
            print(f"{key}, {thing[1]}")
# end of itertools_groupby_test


if __name__ == "__main__":
    print("main")
    # itertools_yield_test()
    # itertools_count_test()
    # itertools_filterfalse_test()
    # itertools_groupby_test()