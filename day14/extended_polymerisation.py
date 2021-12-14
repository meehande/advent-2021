def read_input(filename='test_input.txt'):
    initial_input = []
    transformations = []
    with open(filename, 'r') as f:
        initial_input = [c for c in f.readline().strip()]

        f.readline()  # empty line

        while line := f.readline():
            t = line.strip().split(' -> ')
            transformations.append(tuple(t))
    return initial_input, transformations


def apply_templates(initial_chars, templates):
    initial_chars = list(initial_chars)
    opairs = {}
    pairs = []
    new_pairs = []
    tdict = {k: v for k, v in templates}
    for i in range(len(initial_chars)-1):
        #pairs[f'{initial_chars[i]}{initial_chars[i+1]}'] = f'{initial_chars[i]}{initial_chars[i+1]}'
        pairs.append(f'{initial_chars[i]}{initial_chars[i+1]}')

    init_char = pairs[0][0]
    final_char = pairs[-1][-1]
    for i in range(len(pairs)):
        if replacement := tdict.get(pairs[i], False):
            #pairs[i] = f'{pairs[0]}{replacement}'
            pairs[i] = f'{replacement}{pairs[i][1]}'

    return f'{init_char}{"".join(pairs)}'

    for pattern, replacement in tdict.items():
        if pattern in pairs.keys():
            pairs[pattern] = f'{pattern[0]}{replacement}{pattern[1]}'[:2]
    return ''.join(list(pairs.values())) + 'B'
    return list(pairs.keys())[-1][-1]


i, t = read_input('input.txt')

for _ in range(10):
    i = apply_templates(i, t)

print(i)

counts = {}
for letter in set(i):
    counts[letter] = i.count(letter)

print(max(counts.values()) - min(counts.values()))




