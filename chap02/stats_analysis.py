import pstats

if __name__ == '__main__':
    p = pstats.Stats("profile.stats")
    p.sort_stats("cumulative")

    print("print_stats")
    p.print_stats()
    print()

    print("print_callers")
    p.print_callers()
    print()

    print("print_callees")
    p.print_callees()
    print()