

def lowest_cost_horizontal(positions):
    scale = max(positions)
    position_frequency = [0]*(scale + 1)

    for p in positions:
        position_frequency[p] += 1

    curr_cost = scale*len(positions) + 1
    return calculate_cost(scale//2, position_frequency, scale, curr_cost)


def calculate_cost(mid, position_frequency, scale, curr_cost):
    distance_left = sum([position_frequency[i] * (mid - i) for i in range(mid)])
    distance_right = sum([position_frequency[i] * (i - mid) for i in range(mid, scale + 1)])

    new_cost = distance_left + distance_right
    if new_cost > curr_cost:
        return curr_cost, mid

    curr_cost = new_cost

    if distance_left > distance_right:
        mid = mid // 2
    elif distance_left == distance_right:
        print('equal, going left')
        mid = mid // 2
    else:
        mid = mid + (mid // 2)
    print(f'moving to {mid}')
    return calculate_cost(mid, position_frequency, scale, curr_cost)
#435004  # 51386


def brute_force(positions):
    scale = max(positions)
    position_frequency = [0]*(scale + 1)

    for p in positions:
        position_frequency[p] += 1

    lowest_cost = scale*len(positions) + 1
    best_position = 0
    costs = {}
    for curr_location in range(scale+1):
        new_cost = sum([position_frequency[i] * abs(curr_location - i) for i in range(scale+1)])
        costs[curr_location] = new_cost
        if new_cost < lowest_cost:
            lowest_cost = new_cost
            best_position = curr_location
    return lowest_cost, best_position, costs

input = [int(i) for i in open('input.txt', 'r').readline().split(',')]
brute_force(input)


cost, position = lowest_cost_horizontal([16,1,2,0,4,2,7,1,2,14])
#'51386'  #335942


