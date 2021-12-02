

def forward(h, d, a, v):
    return h+v, d+(a*v), a


def up(h, d, a, v):
    return h, d, a-v


def down(h, d, a, v):
    return h, d, a+v


STEP_MAP = {
    'forward': forward,
    'down': down,
    'up': up,
}

with open("advent/day2/input.txt", "r") as f:
    horizontal = 0
    depth = 0
    aim = 0
    while next_step := f.readline():
        direction, distance = next_step.split(' ')
        step_fn = STEP_MAP[direction.strip()]
        horizontal, depth, aim = step_fn(horizontal, depth, aim, int(distance.strip()))

    print(horizontal, depth, aim)
    print(horizontal*depth)
