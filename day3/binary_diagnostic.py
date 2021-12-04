import numpy as np


def power(file_path):
    with open(file_path, 'r') as f:
        init = f.readline()
        count = np.array([int(c) for c in init.strip()])
        nvalues = 1
        while nextline := f.readline():
            count += [int(c) for c in nextline.strip()]
            nvalues += 1

    most_common = ((count / nvalues)>=0.5).astype(int)
    print('most_common: ', most_common)
    gamma = int(''.join([str(m) for m in most_common]), 2)

    least_common = ((count / nvalues)<=0.5).astype(int)
    print('least_common: ', least_common)
    epsilon = int(''.join([str(l) for l in least_common]), 2)

    power = epsilon*gamma
    print(gamma, epsilon, power)
    return power


power('test_input.txt')


def oxygen_generator(file_path):

    input_arr = np.array([np.array([int(c) for c in x.rstrip()]) for x in open(file_path)])
    _, ncols = input_arr.shape

    oxy_gen = input_arr.copy()
    co2_scrub = input_arr.copy()

    for col in range(ncols):
        orows = oxy_gen.shape[0]
        if orows > 1:
            mstcommon_or_one = int(oxy_gen[:, col].sum()/orows >= 0.5)
            oxy_gen = oxy_gen[oxy_gen[:,col]==mstcommon_or_one]

        crows = co2_scrub.shape[0]
        if crows > 1:
            lstcommon_or_zero = int(not(co2_scrub[:, col].sum() / crows >= 0.5))
            co2_scrub = co2_scrub[co2_scrub[:,col] == lstcommon_or_zero]

    oxy_dec = int(''.join([str(l) for l in list(oxy_gen[0])]), 2)
    co2_dec = int(''.join([str(l) for l in list(co2_scrub[0])]), 2)

    life_support = oxy_dec * co2_dec
    print(oxy_dec, co2_dec, life_support)

oxygen_generator('input.txt')