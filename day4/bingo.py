import numpy as np
from collections import defaultdict


def read_input(filepath):
    with open(filepath, 'r') as f:
        numbers = [int(n) for n in f.readline().split(',')]
        boards = []
        board = []
        while nextline := f.readline():
            nextline = nextline.strip().split(' ')
            if nextline == '' or nextline == ['']:
                if len(board):
                    boards.append(np.array(board))
                board = []
            else:
                board.append([int(n) for n in nextline if n!=''])
        return numbers, boards


def is_winner(board: np.array):
    return any((board < 0).all(axis=0)) or any((board < 0).all(axis=1))


def calculate_result(number, board):

    return board[(board>0)].sum() * number


def play_bingo(numbers, boards):
    winning_board = None
    winning_number = -1
    for number in numbers:
        for board in boards:
            matches = np.where(board == number)
            if len(matches[0]) > 0:
                for x, y in zip(matches[0], matches[1]):
                    board[x, y] *= -1
                if is_winner(board):
                    winning_board = board
                    winning_number = number
                    break
    res = calculate_result(winning_number, winning_board)
    print(res)
    return res


def winning_number(numbers, board):
    for number in numbers:
        matches = np.where(board == number)
        if len(matches[0]) > 0:
            for x, y in zip(matches[0], matches[1]):
                board[x, y] *= -1
            if is_winner(board):
                return number, numbers.index(number)


def losing_board(numbers, boards):
    winning_order = defaultdict(list)
    for board in boards:
        n, nidx = winning_number(numbers, board)
        winning_order[nidx].append(board)
    n = max(winning_order.keys())
    b = winning_order[n]

    res = calculate_result(numbers[n], b)
    return res


n, boards = read_input('input.txt')
r = losing_board(n, boards)
n, boards = read_input('input.txt')
r = play_bingo(n, boards)

