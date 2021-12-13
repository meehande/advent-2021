import numpy as np


def transformation(point, fold, fold_axis):
    if fold_axis == 'x':
        xt = point[0] - 2*(point[0]-fold)
        yt = point[1]
    else:
        xt = point[0]
        yt = point[1] - 2 * (point[1] - fold)
    # eg folding point x_t = 14 through x=7 results in x_t=0
    return (xt, yt)

points = []
folds = []
with open('input.txt', 'r') as f:
    while line := f.readline().strip():
        points.append(tuple([int(i) for i in line.strip().split(',')]))
    # hits newline between points and folds
    while line := f.readline().strip():
        if 'fold along' in line:
            folds.append(tuple(line.strip().strip('fold along ').split('=')))


print(len(points))


def apply_fold(points, fold_value, fold_axis):
    if fold_axis == 'x':
        coord = 0
    else:
        coord = 1
    transformed_points = []
    for point in points:
        if point[coord] <= fold_value:
            transformed_points.append(point)
        else:
            transformed_points.append((transformation(point, fold_value, fold_axis)))
    return transformed_points

# part one
# initial_fold = folds[0]
# t = apply_fold(points,  int(initial_fold[1]), initial_fold[0])
# print(len(set(t)))


# part two
t = [p for p in points]
for fold in folds:
    t = apply_fold(t, int(fold[1]), fold[0])

print(len(set(t)))


def fill_grid(transformed_points):
    max_x = max([p[0] for p in transformed_points])
    max_y = max([p[1] for p in transformed_points])
    grid = [['*']*(max_x+1)]*(max_y+1)
    grid = np.array(grid)
    for p in transformed_points:
        grid[p[1]][p[0]] = '#'
    return [list(g) for g in grid]



grid = fill_grid(set(t))
[print(g) for g in grid]


