import time
from functools import wraps

# area of the complex space to be analyzed
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8

c_real, c_imag = -0.62772, -.42193


def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2=time.time()
        print('Function {} is working, it took {} seconds'.format(fn.__name__, t2-t1))

        return result

    return measure_time

#@timefn
@profile
def calculate_z_serial_purepython(maxiter, zs, cs):
    """Counting output list using julia collection update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output


def calc_pure_python(desired_width, max_iterations):
    """Create list of complex coordinates and complex parameters (cs), building julia set ans printing data"""
    x_step = (float(x2 - x1) / float(desired_width))
    y_step = (float(y1 - y2) / float(desired_width))
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

    cs = []
    zs = []

    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))
    print('Longitude for x: {}'.format(len(x)))
    print('Number of elements: {}'.format(len(zs)))
    output = calculate_z_serial_purepython(max_iterations, zs, cs)


if __name__ == '__name__':
    """example 2.3 counting julia set using pure python with reasonable parameters for laptop"""
    calc_pure_python(desired_width=1000, max_iterations=300)

calc_pure_python(desired_width=1000, max_iterations=100)
