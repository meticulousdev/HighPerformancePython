class Point01(object):
    def __init__(self, x, y):
        self.x, self.y = x, y


class Point02(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    p1_01 = Point01(1, 1)
    p1_02 = Point01(1, 1)
    print(set([p1_01, p1_02]))
    print(Point01(1, 1) in set([p1_01, p1_02]))

    p2_01 = Point02(1, 1)
    p2_02 = Point02(1, 1)
    print(set([p2_01, p2_02]))    
    print(Point02(1, 1) in set([p2_01, p2_02]))
