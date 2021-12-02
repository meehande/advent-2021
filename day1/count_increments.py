import pandas as pd


def part_one(numbers):
    """
    count the number of increments in the input list of nums
    """
    df = pd.DataFrame(numbers, columns=['number'])

    num_increments = sum((df['number'] - df['number'].shift()) > 0)
    print(num_increments)
    return num_increments


def part_two(numbers):
    """
    count the number of (summed-3-value-window) increments in the input list of nums
    """
    first = sum(numbers[0:3])
    increments = 0
    for i in range(1, len(numbers)-2):
        second = sum(numbers[i:i + 3])
        increments += int((second - first) > 0)
        first = second
    print(increments)
    return increments


numbers = [int(x.rstrip()) for x in open('advent/day1/input.txt')]

part_one(numbers)

part_two(numbers)