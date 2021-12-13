import numpy as np

def compute_slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)


def y_intercept(x, y, m):
    # y = mx+c
    return y-(m*x)


def compute_line_eqn(x1, y1, x2, y2):
    m = compute_slope(x1, y1, x2, y2)
    c = y_intercept(x1, y1, m)

    return m, c


def line_intercept(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Px = (x1y2 - y1x2)(x3-x4) - (x1-x2)(x3y4 - y3x4) / D
    Py = (x1y2 - y1x2)(y3-y4) - (y1-y2)(x3y4 - y3x4) / D

    D = (x1 - x2)(y3 - y4) - (y1 - y2)(x3 - x4)
    """
    d = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4))/d
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4))/d
    return px, py


def fill_grid(points, mx, my):
    dim = max(mx, my)
    grid = np.zeros((dim, dim))
    for line in points:
        x1, y1, x2, y2 = line
        if x1 == x2:
            start = min(y1, y2)
            end = max(y1, y2)
            grid[start:end+1, x1] += 1
        if y1 == y2:
            start = min(x1, x2)
            end = max(x1, x2)
            end = min(end+1, mx)
            grid[y1, start:end+1] += 1
    return len(np.where(grid >= 2)[0]), grid


def read_points(fileinput):
    points = []
    max_x, max_y = 0, 0
    with open(fileinput, 'r') as f:
        while line := f.readline():
            p1, p2 = line.split('->')
            point = tuple(int(p) for p in [*p1.strip().split(','), *p2.strip().split(',')])
            max_x = max(point[0], max_x)
            max_x = max(point[2], max_x)
            max_y = max(point[1], max_y)
            max_y = max(point[3], max_y)
            points.append(point)

    return points, max_x+1, max_y+1


points, max_x, max_y = read_points('test_input.txt')
intercepts, grid = fill_grid(points, max_x, max_y)
