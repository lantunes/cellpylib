import numpy as np

import matplotlib.pyplot as plt


def plot(ca):
    cmap = plt.get_cmap('Greys')
    plt.imshow(ca, interpolation='none', cmap=cmap)
    plt.show()


def evolve(cellular_automaton, n_steps, apply_rule, r=1):
    _, cols = cellular_automaton.shape
    array = np.zeros((n_steps, cols), dtype=np.byte)
    array[0] = cellular_automaton

    def index_strides(arr, window_size):
        # this function is based on code in http://www.credid.io/cellular-automata-python-2.html
        arr = np.concatenate((arr[-window_size//2+1:], arr, arr[:window_size//2]))
        shape = arr.shape[:-1] + (arr.shape[-1] - window_size + 1, window_size)
        strides = arr.strides + (arr.strides[-1],)
        return np.lib.stride_tricks.as_strided(arr, shape=shape, strides=strides)

    for i in range(1, n_steps):
        cells = array[i - 1]
        strides = index_strides(np.arange(len(cells)), 2*r + 1)
        states = cells[strides]
        array[i] = np.array([apply_rule(s, c) for c, s in enumerate(states)])
    return array


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
    """
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
    """
    state_int = bits_to_int(state)
    n = 2**len(state)
    rule_bin_array = int_to_bits(rule, n)
    return rule_bin_array[(n-1) - state_int]


def number_rule(state, rule):
    """
    The same idea as the NKS rule, except that the neighbourhoods are listed in 
      lexicographic order (the reverse of the NKS convention).
    :param state: a binary array of length 2r + 1
    :param rule: an int indicating the cellular automaton rule number
    :return: the result, 0 or 1, of applying the given rule on the given state
    """
    state_int = bits_to_int(state)
    rule_bin_array = int_to_bits(rule, 2**len(state))
    return rule_bin_array[state_int]


def init_simple(size):
    x = np.zeros(size, dtype=np.byte)
    x[len(x)//2] = 1
    return np.array([x])


def init_random(size):
    return np.array([np.random.randint(2, size=size, dtype=np.byte)])
