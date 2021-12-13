from collections import deque, defaultdict

VERTICES = defaultdict(list)

with open('input.txt', 'r') as f:
    while edge := f.readline():
        src, dst = edge.strip().split('-')
        VERTICES[src].append(dst)
        VERTICES[dst].append(src)


def part_1():
    # bfs with keeping the visited list per path
    start = ('start', set(['start']))
    npaths = 0

    to_process = deque([start])
    while to_process:
        curr_vertex, visited = to_process.popleft()

        if curr_vertex == 'end':
            npaths += 1
            continue

        for n in VERTICES[curr_vertex]:
            if n not in visited:
                new_visited = set(visited)
                if n.islower():
                    new_visited.add(n)
                to_process.append((n, new_visited))
    return npaths


def part_2():
    # bfs with keeping the visited list per path
    start = ('start', set(['start']), None)
    npaths = 0

    to_process = deque([start])
    while to_process:
        curr_vertex, visited, visited_twice = to_process.popleft()

        if curr_vertex == 'end':
            npaths += 1
            continue

        for n in VERTICES[curr_vertex]:
            if n not in visited:
                new_visited = set(visited)
                if n.islower():
                    new_visited.add(n)
                to_process.append((n, new_visited, visited_twice))
            elif (n in visited) and (visited_twice is None) and (n not in ['start', 'end']):
                to_process.append((n, visited, n))
    return npaths


p = part_1()
p = part_2()




