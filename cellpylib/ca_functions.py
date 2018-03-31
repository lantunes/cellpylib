import matplotlib.pyplot as plt
import numpy as np


def plot(ca, title=''):
    cmap = plt.get_cmap('Greys')
    plt.title(title)
    plt.imshow(ca, interpolation='none', cmap=cmap)
    plt.show()


def plot_multiple(ca_list, titles):
    cmap = plt.get_cmap('Greys')
    for i in range(0, len(ca_list)):
        plt.figure(i)
        plt.title(titles[i])
        plt.imshow(ca_list[i], interpolation='none', cmap=cmap)
    plt.show()


def evolve(cellular_automaton, n_steps, apply_rule, r=1):
    _, cols = cellular_automaton.shape
    array = np.zeros((n_steps, cols), dtype=np.int)
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


def binary_rule(state, rule, scheme=None):
    """
    Converts the given rule number to a binary representation, and uses this to determine the value to return.
    The process is approximately described as:
    1. convert state to int, so [1,0,1] -> 5, call this state_int
    2. convert rule to binary, so 254 -> [1,1,1,1,1,1,1,0], call this rule_bin_array
    3. new value is rule_bin_array[7 - state_int]
         we subtract 7 from state_int to be consistent with the numbering scheme used in NKS
         in NKS, rule 254 for a 1D binary cellular automaton is described as:
        [1,1,1]  [1,1,0]  [1,0,1]  [1,0,0]  [0,1,1]  [0,1,0]  [0,0,1]  [0,0,0]
           1        1        1        1        1        1        1        0
    If None is provided for the scheme parameter, the neighbourhoods are listed in lexicographic order (the reverse of 
    the NKS convention). If 'nks' is provided for the scheme parameter, the NKS convention is used for listing the 
    neighbourhoods.
    :param state: a binary array of length 2r + 1
    :param rule: an int indicating the cellular automaton rule number
    :param scheme: can be None (default) or 'nks'; if 'nks' is given, the rule numbering scheme used in NKS is used
    :return: the result, 0 or 1, of applying the given rule on the given state
    """
    state_int = bits_to_int(state)
    n = 2**len(state)
    rule_bin_array = int_to_bits(rule, n)
    if scheme == 'nks':
        return rule_bin_array[(n-1) - state_int]
    return rule_bin_array[state_int]


def nks_rule(state, rule):
    """
    A convenience function, that calls binary_rule with scheme = 'nks'.
    :param state: a binary array of length 2r + 1
    :param rule: an int indicating the cellular automaton rule number
    :return: 
    """
    return binary_rule(state, rule, scheme='nks')


def totalistic_rule(state, k, rule):
    """
    The totalistic rule as described in NKS. The average color is mapped to a whole number in [0, k - 1].
    The rule number is in base 10, but interpreted in base k. For a 1-dimensional cellular automaton, there are
    3k - 2 possible average colors in the cell neighbourhood.
    :param state: a k-color array of length 2r + 1
    :param k: the number of colors in this cellular automaton, where only 2 <= k <= 36 is supported
    :param rule: the k-color cellular automaton rule number in base 10, interpreted in base k
    :return: the result, a number from 0 to k - 1, of applying the given rule on the given state
    """
    # e.g. np.base_repr(777, base=3) -> '1001210'; the zfill pads the string with zeroes: '1'.zfill(3) -> '001'
    #   Bases greater than 36 not handled in base_repr.
    rule_string = np.base_repr(rule, base=k).zfill(3*k - 2)
    if len(rule_string) > 3*k - 2:
        raise Exception("rule number out of range")
    state_sum = sum(state)
    # the rightmost element of the rule is for the average color 0, in NKS convention
    return int(rule_string[(3*k - 3) - state_sum], k)


def init_simple(size, val=1):
    """
    Returns an array initialized with zeroes, with its center value set to the specified value, or 1 by default.
    :param size: the size of the array to be created 
    :param val: the value to be used in the center of the array (1, by default)
    :return: a vector with shape (1, size), with its center value initialized to the specified value, or 1 by default 
    """
    x = np.zeros(size, dtype=np.int)
    x[len(x)//2] = val
    return np.array([x])


def init_random(size, k=2, n_randomized=None, empty_value=0):
    """
    Returns a randomly initialized array with values consisting of numbers in {0,...,k - 1}, where k = 2 by default.
    :param size: the size of the array to be created
    :param k: the number of states in the cellular automaton (2, by default)
    :param n_randomized: the number of randomized sites in the array; this value must be >= 0 and <= size, if specified; 
                         if this value is not specified, all sites in the array will be randomized; the randomized sites
                         will be centered in the array, while all others will have an empty value
    :param empty_value: the value to use for non-randomized sites (0, by default)
    :return: a vector with shape (1, size), randomly initialized with numbers in {0,...,k - 1}
    """
    if n_randomized is None:
        n_randomized = size
    if n_randomized > size or n_randomized < 0:
        raise Exception("the number of randomized sites, if specified, must be >= 0 and <= size")
    pad_left = (size - n_randomized) // 2
    pad_right = (size - n_randomized) - pad_left
    return np.array([np.pad(np.array(np.random.randint(k, size=n_randomized, dtype=np.int)), (pad_left, pad_right),
                            'constant', constant_values=empty_value)])
