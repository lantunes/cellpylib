import numpy as np

import matplotlib.pyplot as plt


def plot_ca(ca):
    cmap = plt.get_cmap('Greys')
    plt.imshow(ca, interpolation='none', cmap=cmap)
    plt.show()


def step(array, apply_rule):
    rows, cols = array.shape
    for i in range(1, rows):
        for j in range(1, cols):
            state = array[i-1, j-1:j+2]
            array[i, j] = apply_rule(state)


def bits_to_int(bits):
    total = 0
    for shift, j in enumerate(bits[::-1]):
        if j:
            total += 1 << shift
    return total


def int_to_bits(num, num_digits):
    converted = list(map(int, bin(num)[2:]))
    return np.pad(converted, (num_digits - len(converted), 0), 'constant')


def nks_rule(state, rule):
    '''
    convert state to int, so [1,0,1] -> 5, call this state_int
    convert rule to binary, so 254 -> [1,1,1,1,1,1,1,0], call this rule_bin_array
    new value is rule_bin_array[7 - state_int]
      we subtract 7 from state_int to be consistent with the numbering scheme used in NKS
      in NKS, rule 254 for a 1D binary cellular automaton is described as:
        [1,1,1]  [1,1,0]  [1,0,1]  [1,0,0]  [0,1,1]  [0,1,0]  [0,0,1]  [0,0,0]
           1        1        1        1        1        1        1        0
    :param state: a binary array of length 3
    :param rule: an int, from 0 to 255, indicating the cellular automaton rule number in NKS convention
    :return: the result, 0 or 1, of applying the given NKS rule on the given state 
    '''
    state_int = bits_to_int(state)
    rule_bin_array = int_to_bits(rule, 8)
    return rule_bin_array[7 - state_int]


def start_one_bit(size):
    x = np.zeros(size, dtype=np.int)
    x[len(x)//2] = 1
    return x


def start_random(size):
    return np.random.randint(2, size=size)


def create_ca(rows, cols, start):
    ca = np.zeros((rows, cols))
    ca[0] = start
    return ca
