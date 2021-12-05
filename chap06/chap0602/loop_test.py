from math import sin


def loop_slow(num_iteartions):
    result = 0
    for i in range(num_iteartions):
        result += i * sin(num_iteartions)
    return result


def loop_fast(num_iteartions):
    result = 0
    factor = sin(num_iteartions)
    for i in range(num_iteartions):
        result += i
    return result * factor


if __name__ == "__main__":
    print(loop_slow(int(1e4)))
    print(loop_fast(int(1e4)))
