import numpy as np


def move(ar: np.array, symbol: str):
    i = 0
    first_val = ar[0]
    while i < len(ar):
        if ar[i] == symbol:
            if i < (len(ar) - 1):
                nextpos = i + 1
                if ar[nextpos] == '.':
                    ar[i] = '.'
                    ar[nextpos] = symbol
                    i += 1
            else:
                nextpos = 0
                if first_val == '.':
                    ar[i] = '.'
                    ar[nextpos] = symbol
                    i += 1
        i += 1
    return ar


def read_input(filename):
    gridlines = []
    with open(filename, 'r') as f:
        while next_line := f.readline():
            gridlines.append(next_line.strip())
    ar = np.array([np.array([c for c in r]) for r in gridlines])
    return ar


far = read_input('input.txt')

prev = np.full(far.shape, '.')
niter = 0
while not((prev == far).all()):
    prev = np.copy(far)

    for m in range(far.shape[0]):
        far[m,:] = move(far[m,:], '>')
    for n in range(far.shape[1]):
        far[:, n] = move(far[:,n], 'v')
    niter += 1
print(niter)
print(far)

r = np.array(['v', '.', '.', '.', '>', '>', '.', 'v', 'v', '>'])
t=move_east(r)