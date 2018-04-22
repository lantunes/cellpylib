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


def evolve(cellular_automaton, timesteps, apply_rule, r=1):
    """
    Evolves the given cellular automaton for the specified time steps. Applies the given function to each cell during
    the evolution. A cellular automaton is represented here as an array of arrays, or matrix. This function expects
    an array containing the initial time step (i.e. initial condition, an array) for the cellular automaton. The final
    result is a matrix, where the number of rows equal the number of time steps specified.
    :param cellular_automaton: the cellular automaton starting condition representing the first time step; 
                               e.g. [[0,0,0,0,1,0,0,0,0]] 
    :param timesteps: the number of time steps in this evolution; note that this value refers to the total number of
                      time steps in this cellular automaton evolution, which includes the initial condition  
    :param apply_rule: a function representing the rule to be applied to each cell during the evolution; this function
                       will be given three arguments, in the following order: the neighbourhood, which is a numpy array
                       of length 2r + 1 representing the neighbourhood of the cell; the cell identity, which is a scalar
                       representing the index of the cell in the cellular automaton array; the time step, which is a 
                       scalar representing the time step in the evolution
    :param r: the neighbourhood radius; the neighbourhood size will be 2r + 1
    :return: a matrix, containing the results of the evolution, where the number of rows equal the number of time steps 
             specified
    """
    _, cols = cellular_automaton.shape
    array = np.zeros((timesteps, cols), dtype=cellular_automaton.dtype)
    array[0] = cellular_automaton

    def index_strides(arr, window_size):
        # this function is based on code in http://www.credid.io/cellular-automata-python-2.html
        arr = np.concatenate((arr[-window_size//2+1:], arr, arr[:window_size//2]))
        shape = arr.shape[:-1] + (arr.shape[-1] - window_size + 1, window_size)
        strides = arr.strides + (arr.strides[-1],)
        return np.lib.stride_tricks.as_strided(arr, shape=shape, strides=strides)

    for t in range(1, timesteps):
        cells = array[t - 1]
        strides = index_strides(np.arange(len(cells)), 2*r + 1)
        neighbourhoods = cells[strides]
        array[t] = np.array([apply_rule(n, c, t) for c, n in enumerate(neighbourhoods)])
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


def binary_rule(neighbourhood, rule, scheme=None):
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
    :param neighbourhood: a binary array of length 2r + 1
    :param rule: an int indicating the cellular automaton rule number
    :param scheme: can be None (default) or 'nks'; if 'nks' is given, the rule numbering scheme used in NKS is used
    :return: the result, 0 or 1, of applying the given rule on the given state
    """
    state_int = bits_to_int(neighbourhood)
    n = 2**len(neighbourhood)
    rule_bin_array = int_to_bits(rule, n)
    if scheme == 'nks':
        return rule_bin_array[(n-1) - state_int]
    return rule_bin_array[state_int]


def nks_rule(neighbourhood, rule):
    """
    A convenience function, that calls binary_rule with scheme = 'nks'.
    :param neighbourhood: a binary array of length 2r + 1
    :param rule: an int indicating the cellular automaton rule number
    :return: 
    """
    return binary_rule(neighbourhood, rule, scheme='nks')


def totalistic_rule(neighbourhood, k, rule):
    """
    The totalistic rule as described in NKS. The average color is mapped to a whole number in [0, k - 1].
    The rule number is in base 10, but interpreted in base k. For a 1-dimensional cellular automaton, there are
    3k - 2 possible average colors in the 3-cell neighbourhood. There are n(k - 1) + 1 possible average colors for a 
    k-color cellular automaton with an n-cell neighbourhood.
    :param neighbourhood: a k-color array of any size
    :param k: the number of colors in this cellular automaton, where only 2 <= k <= 36 is supported
    :param rule: the k-color cellular automaton rule number in base 10, interpreted in base k
    :return: the result, a number from 0 to k - 1, of applying the given rule on the given state
    """
    # e.g. np.base_repr(777, base=3) -> '1001210'; the zfill pads the string with zeroes: '1'.zfill(3) -> '001'
    #   Bases greater than 36 not handled in base_repr.
    n = neighbourhood.size
    rule_string = np.base_repr(rule, base=k).zfill(n*(k - 1) + 1)
    if len(rule_string) > n*(k - 1) + 1:
        raise Exception("rule number out of range")
    neighbourhood_sum = np.sum(neighbourhood)
    # the rightmost element of the rule is for the average color 0, in NKS convention
    return int(rule_string[n*(k - 1) - neighbourhood_sum], k)


def init_simple(size, val=1, dtype=np.int):
    """
    Returns an array initialized with zeroes, with its center value set to the specified value, or 1 by default.
    :param size: the size of the array to be created 
    :param val: the value to be used in the center of the array (1, by default)
    :param dtype: the data type
    :return: a vector with shape (1, size), with its center value initialized to the specified value, or 1 by default 
    """
    x = np.zeros(size, dtype=dtype)
    x[len(x)//2] = val
    return np.array([x])


def init_random(size, k=2, n_randomized=None, empty_value=0, dtype=np.int):
    """
    Returns a randomly initialized array with values consisting of numbers in {0,...,k - 1}, where k = 2 by default.
    If dtype is not an integer type, then values will be uniformly distributed over the half-open interval [0, k - 1).
    :param size: the size of the array to be created
    :param k: the number of states in the cellular automaton (2, by default)
    :param n_randomized: the number of randomized sites in the array; this value must be >= 0 and <= size, if specified; 
                         if this value is not specified, all sites in the array will be randomized; the randomized sites
                         will be centered in the array, while all others will have an empty value
    :param empty_value: the value to use for non-randomized sites (0, by default)
    :param dtype: the data type
    :return: a vector with shape (1, size), randomly initialized with numbers in {0,...,k - 1}
    """
    if n_randomized is None:
        n_randomized = size
    if n_randomized > size or n_randomized < 0:
        raise Exception("the number of randomized sites, if specified, must be >= 0 and <= size")
    pad_left = (size - n_randomized) // 2
    pad_right = (size - n_randomized) - pad_left
    if np.issubdtype(dtype, np.integer):
        rand_nums = np.random.randint(k, size=n_randomized, dtype=dtype)
    else:
        rand_nums = np.random.uniform(0, k - 1, size=n_randomized).astype(dtype)
    return np.array([np.pad(np.array(rand_nums), (pad_left, pad_right), 'constant', constant_values=empty_value)])


class ReversibleRule:
    """
    An elementary cellular automaton rule explicitly set up to be reversible.
    """
    def __init__(self, init_state, rule_number):
        """
        Creates a reversible elementary cellular automata rule by taking into consideration the previous state of a 
        cell, by taking the XOR of the rule's normal output with the previous state to get the new state.
        :param init_state: a vector representing the initial previous state of the cells, consisting of binary values
        :param rule_number: the elementary cellular automata rule number to be used, in NKS convention
        """
        self._previous_state = init_state
        self._rule_number = rule_number

    def apply_rule(self, n, c, t):
        regular_result = nks_rule(n, self._rule_number)
        new_result = regular_result ^ self._previous_state[c]
        self._previous_state[c] = n[len(n) // 2]
        return new_result


class AsynchronousRule:
    """
    Creates an asynchronous cellular automaton rule with a cyclic update scheme. Also known as a sequential cellular
    automaton rule, in NKS. This rule wraps a given rule, making the given rule asynchronous. This rule works for 
    both 1D and 2D cellular automata.
    """
    def __init__(self, apply_rule, update_order=None, num_cells=None, randomize_each_cycle=False):
        """
        Constructs an asynchronous rule out of a given rule. Either the update_order or num_cells parameter must be
        specified. If no update_order is given, then the num_cells parameter must be specified, and an update order
        list will be constructed and shuffled.
        :param apply_rule: the rule that will be made asynchronous
        :param update_order: a list containing the indices of the cells in the CA, specifying the update order; if the
                             CA is 2D, then the indices will refer to the cells in the matrix as if the matrix were an
                             array (e.g. for a 2x3 2D CA, the mapping from cell coordinate to cell index is: 
                             (0,0)->0, (0,1)->1, (0,2)->2, (1,0)->3, (1,1)->4, (1,2)->5)
        :param num_cells: the total number of cells in the CA
        :param randomize_each_cycle: whether to shuffle the update order list after each complete cycle
        """
        if update_order is None and num_cells is None:
            raise Exception("either update_order or num_cells must be specified")
        self._apply_rule = apply_rule
        if update_order is not None:
            self._update_order = update_order
        else:
            self._shuffle_update_order(num_cells)
        self._curr = 0
        self._num_applied = 0
        self._randomize_each_cycle = randomize_each_cycle

    def _shuffle_update_order(self, num_cells):
        self._update_order = np.arange(num_cells)
        np.random.shuffle(self._update_order)
        self._update_order = self._update_order.tolist()

    def apply_rule(self, n, c, t):
        if self._in_update_order(c, n):
            self._num_applied += 1
        if not self._should_update(c, n):
            self._check_for_end_of_cycle()
            return self._current_cell_value(n)
        self._check_for_end_of_cycle()
        return self._apply_rule(n, c, t)

    def _in_update_order(self, c, n):
        if len(n.shape) == 1:
            return c in self._update_order
        elif len(n.shape) == 2:
            i = c[0]*n.shape[1] + c[1]  # convert matrix coordinates to array index
            return i in self._update_order
        else:
            raise Exception("unexpected neighbourhood dimensions: %s" % n.shape)

    def _should_update(self, c, n):
        if len(n.shape) == 1:
            return c == self._update_order[self._curr]
        elif len(n.shape) == 2:
            i = c[0]*n.shape[1] + c[1]  # convert matrix coordinates to array index
            return i == self._update_order[self._curr]
        else:
            raise Exception("unexpected neighbourhood dimensions: %s" % n.shape)

    def _check_for_end_of_cycle(self):
        if self._num_applied == len(self._update_order):
            self._curr = (self._curr + 1) % len(self._update_order)
            self._num_applied = 0
            if self._randomize_each_cycle:
                self._shuffle_update_order(len(self._update_order))

    def _current_cell_value(self, n):
        if len(n.shape) == 1:
            return n[len(n)//2]
        elif len(n.shape) == 2:
            return n[n.shape[0]//2][n.shape[1]//2]
        else:
            raise Exception("unexpected neighbourhood dimensions: %s" % n.shape)
