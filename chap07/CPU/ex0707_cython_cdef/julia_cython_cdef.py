import time
import cythonfn_cdef


x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193


def calc_pure_python(desired_width, max_iterations):
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []

    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step

    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs = []
    cs = []

    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print(f"Length of x: {len(x)}")
    print(f"Total elements: {len(zs)}")

    start_time = time.time()

    output = cythonfn_cdef.calculate_z(max_iterations, zs, cs)

    end_time = time.time()

    secs = end_time - start_time
    print(cythonfn_cdef.calculate_z.__name__ + " took", secs, "seconds")

    assert sum(output) == 33219980


if __name__ == "__main__":
    calc_pure_python(desired_width=1000, max_iterations=300)

    # Length of x: 1000
    # Total elements: 1000000
    # calculate_z took 0.3575878143310547 seconds
