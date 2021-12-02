

def forward(h, d, v):
    return h+v, d


def up(h, d, v):
    return h, d-v


def down(h, d, v):
    return h, d+v


STEP_MAP = {
    'forward': forward,
    'down': down,
    'up': up,
}

with open("advent/day2/input.txt", "r") as f:
    horizontal = 0
    depth = 0
    while next_step := f.readline():
        direction, distance = next_step.split(' ')
        step_fn = STEP_MAP[direction.strip()]
        horizontal, depth = step_fn(horizontal, depth, int(distance.strip()))


