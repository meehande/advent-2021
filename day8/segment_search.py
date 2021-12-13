from collections import defaultdict


NUMBER_SEGMENT_LENS = {
    '0': (6, 'abcefg'),  # abcefg
    '1': (2, 'cf'),  # cf
    '2': (5, 'acfeg'),  # acfeg
    '3': (5, 'acdfg'),  # acdfg
    '4': (4, 'bcdf'),  # bcdf
    '5': (5, 'abdfg'),  # abdfg
    '6': (5, 'bdefg'),  # bdefg
    '7': (3, 'acf'),  # acf
    '8': (7, 'abcdefg'),  # abcdefg
    '9': (6, 'abcdfg'),  # abcdfg
}


def calculate_unique_segment_lens():
    """
    dict of len_segments_for_number: number
    :return:
    """
    segment_lens = defaultdict(int)
    segment_len_map = {}
    for slen, n in NUMBER_SEGMENT_LENS.values():
        segment_lens[slen] += 1
        segment_len_map[slen] = n
    unique_segments = [s for s, l in segment_lens.items() if l == 1]
    return {k: v for k, v in segment_len_map.items() if k in unique_segments}


def count_unique_segment_len_output(output_values):
    unique_lens = list(calculate_unique_segment_lens().keys())
    counts = 0
    for o in output_values:
        counts += len([n for n in o if len(n) in unique_lens])
    return counts


def read_input(file_name):
    input_signals = []
    output_values = []
    with open(file_name, 'r') as f:
        while line := f.readline():
            inputs, outputv = line.strip().split('|')
            inputs = [i.strip() for i in inputs.strip().split(' ')]
            outputv = [o.strip() for o in outputv.strip().split(' ')]
            input_signals.append(inputs)
            output_values.append(outputv)

    return input_signals, output_values


i, o =read_input('input.txt')


# part 2
def decode_numbers(input_signals, output_values):
    i = ['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb']
    o = ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']
    mapped_numbers = {

    }



# part 1
v = count_unique_segment_len_output(o)
print(v)


