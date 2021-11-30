import matplotlib.pyplot as plt
import numpy as np


def plot(ca, title='', *, colormap='Greys', xlabel='', ylabel='time', show=True, **imshow_kwargs):
    """
    Plots the given cellular automaton.

    :param ca: the cellular automaton to plot

    :param title: the title to place on the plot (default is empty)

    :param colormap: the colormap to use (default is 'Greys')

    :param xlabel: the label of the x-axis (default is empty)

    :param ylabel: the label of the y-axis (default 'time')

    :param show: show the plot (default is True)

    :param imshow_kwargs: keyword arguments for the Matplotlib `imshow` function
    """
    cmap = plt.get_cmap(colormap)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.imshow(ca, interpolation='none', cmap=cmap, **imshow_kwargs)
    if show:
        plt.show()


def plot_multiple(ca_list, titles, *, colormap='Greys', xlabel='', ylabel='time', show=True, **imshow_kwargs):
    """
    Plots multiple cellular automata separately.

    :param ca_list: a list of cellular automata

    :param titles: the titles to give the plots; there must be one title for each CA

    :param colormap: the colormap to use for the plots (default is 'Greys')

    :param xlabel: the label of the x-axis (default is empty)

    :param ylabel: the label of the y-axis (default 'time')

    :param show: show the plot (default is True)

    :param imshow_kwargs: keyword arguments for the Matplotlib `imshow` function
    """
    cmap = plt.get_cmap(colormap)
    for i in range(0, len(ca_list)):
        plt.figure(i)
        plt.title(titles[i])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.imshow(ca_list[i], interpolation='none', cmap=cmap, **imshow_kwargs)
    if show:
        plt.show()


def evolve(cellular_automaton, timesteps, apply_rule, r=1, memoize=False):
    """
    Evolves the given cellular automaton for the specified time steps. Applies the given function to each cell during
    the evolution. A cellular automaton is represented here as an array of arrays, or matrix. This function expects
    an array containing the initial time step (i.e. initial condition, an array) for the cellular automaton. The final
    result is a matrix, where the number of rows equal the number of time steps specified.

    :param cellular_automaton: the cellular automaton starting condition representing the first time step,
                               e.g. [[0,0,0,0,1,0,0,0,0]], or a history of previous states, with the last item in the
                               given array being the starting condition for the evolution,
                               e.g. [[0,0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0]]

    :param timesteps: the number of time steps in this evolution, or a callable that accepts the cellular automaton
                      (in terms of the history of its evolution) and the current timestep number, and is expected to
                      return a boolean indicating whether the evolution should continue; note that if a number is given,
                      this value refers to the total number of time steps in this cellular automaton evolution, which
                      includes the initial condition

    :param apply_rule: a function representing the rule to be applied to each cell during the evolution; this function
                       will be given three arguments, in the following order: the neighbourhood, which is a numpy array
                       of length 2r + 1 representing the neighbourhood of the cell; the cell identity, which is a scalar
                       representing the index of the cell in the cellular automaton array; the time step, which is a 
                       scalar representing the time step in the evolution

    :param r: the neighbourhood radius; the neighbourhood size will be 2r + 1 (default is 1)

    :param memoize: allowed values are True, False, and "recursive"; if True, then the result of applying the rule on a
                    given neighbourhood will be cached, and used on subsequent invocations of the rule; if "recursive",
                    then a recursive memoized algorithm will be used, in which recursively wider neighbourhoods are
                    cached, along with the result of applying the rule on the cells in the widened neighbourhood; the
                    True and "recursive" options can result in a significant improvement to execution speed if the rule
                    is expensive to invoke; the "recursive" option works best when there are strongly repetitive
                    patterns in the CA, and when the state consists of 2^k cells; if False, then no caching will be
                    used; NOTE: this should only be set to True or "recursive" for rules which do not store any state
                    upon invocation, and for rules which do not depend in the cell index or timestep number (default is
                    False)

    :return: a matrix, containing the results of the evolution, where the number of rows equal the number of time steps
             specified
    """
    if callable(timesteps):
        return _evolve_dynamic(cellular_automaton, timesteps, apply_rule, r, memoize)
    else:
        return _evolve_fixed(cellular_automaton, timesteps, apply_rule, r, memoize)


def _evolve_fixed(cellular_automaton, timesteps, apply_rule, r, memoize):
    """
    Evolves the given cellular automaton for the given number of fixed timesteps.

    :param cellular_automaton: the cellular automaton starting condition representing the first time step,
                               e.g. [[0,0,0,0,1,0,0,0,0]], or a history of previous states, with the last item in the
                               given array being the starting condition for the evolution,
                               e.g. [[0,0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0]]

    :param timesteps: the number of time steps in this evolution; this value refers to the total number of time steps in
                      this cellular automaton evolution, which includes the initial condition

    :param apply_rule: a function representing the rule to be applied to each cell during the evolution; this function
                       will be given three arguments, in the following order: the neighbourhood, which is a numpy array
                       of length 2r + 1 representing the neighbourhood of the cell; the cell identity, which is a scalar
                       representing the index of the cell in the cellular automaton array; the time step, which is a
                       scalar representing the time step in the evolution

    :param r: the neighbourhood radius; the neighbourhood size will be 2r + 1

    :param memoize: the memoization flag; one of True, False, or "recursive"

    :return: a matrix, containing the results of the evolution, where the number of rows equal the number of time steps
             specified
    """
    initial_conditions = cellular_automaton[-1]
    _, cols = cellular_automaton.shape
    array = np.zeros((timesteps, cols), dtype=cellular_automaton.dtype)
    array[0] = initial_conditions
    cell_indices = list(range(len(initial_conditions)))

    memo_table = {}

    for t in range(1, timesteps):
        cells = array[t - 1]
        strides = _index_strides(np.arange(len(cells)), 2 * r + 1)
        neighbourhoods = cells[strides]
        if memoize is "recursive":
            next_state = np.zeros(len(cells), dtype=cellular_automaton.dtype)
            _step(cell_indices, cells, next_state, memo_table, apply_rule, r, t)
            array[t] = next_state
        elif memoize is True:
            array[t] = np.array([_get_memoized(n, c, t, apply_rule, memo_table) for c, n in enumerate(neighbourhoods)])
        elif memoize is False:
            array[t] = np.array([apply_rule(n, c, t) for c, n in enumerate(neighbourhoods)])
        else:
            raise Exception("unsupported memoization option: %s" % memoize)

    return np.concatenate((cellular_automaton, array[1:]), axis=0)


def _evolve_dynamic(cellular_automaton, timesteps, apply_rule, r, memoize):
    """
    Evolves the given cellular automaton for a dynamic number of timesteps.

    :param cellular_automaton: the cellular automaton starting condition representing the first time step,
                               e.g. [[0,0,0,0,1,0,0,0,0]], or a history of previous states, with the last item in the
                               given array being the starting condition for the evolution,
                               e.g. [[0,0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0]]

    :param timesteps: a callable that accepts the cellular automaton (in terms of the history of its evolution) and the
                      current timestep number, and is expected to return a boolean indicating whether the evolution
                      should continue

    :param apply_rule: a function representing the rule to be applied to each cell during the evolution; this function
                       will be given three arguments, in the following order: the neighbourhood, which is a numpy array
                       of length 2r + 1 representing the neighbourhood of the cell; the cell identity, which is a scalar
                       representing the index of the cell in the cellular automaton array; the time step, which is a
                       scalar representing the time step in the evolution

    :param r: the neighbourhood radius; the neighbourhood size will be 2r + 1

    :param memoize: the memoization flag; one of True, False, or "recursive"

    :return: a matrix, containing the results of the evolution, where the number of rows equal the number of time steps
             specified
    """
    initial_conditions = cellular_automaton[-1]
    _, cols = cellular_automaton.shape
    array = [initial_conditions]
    cell_indices = list(range(len(initial_conditions)))

    memo_table = {}

    t = 1
    while timesteps(np.array(array), t):
        cells = array[-1]
        strides = _index_strides(np.arange(len(cells)), 2 * r + 1)
        neighbourhoods = cells[strides]
        if memoize is "recursive":
            result = np.zeros(len(cells), dtype=cellular_automaton.dtype)
            _step(cell_indices, cells, result, memo_table, apply_rule, r, t)
        elif memoize is True:
            result = [_get_memoized(n, c, t, apply_rule, memo_table) for c, n in enumerate(neighbourhoods)]
        elif memoize is False:
            result = [apply_rule(n, c, t) for c, n in enumerate(neighbourhoods)]
        else:
            raise Exception("unsupported memoization option: %s" % memoize)
        array.append(np.array(result, dtype=cellular_automaton.dtype))
        t += 1

    return np.concatenate((cellular_automaton, array[1:]), axis=0)


def _step(indices, curr_state, next_state, cache, apply_rule, r, t):
    """
    Perform an update on the given next state using the current state and memoization cache, based on
    an even split of the cell indices.

    :param indices: a list of the cell indices of the cells to update

    :param curr_state: the current state (i.e. the state after the previous timestep)

    :param next_state: the next state (i.e. the result after the current timestep)

    :param cache: a dictionary that maps state neighbourhoods to their activities

    :param apply_rule: the rule to apply during each cell update

    :param r: the neighbourhood radius

    :param t: the current timestep
    """
    mid = len(indices) // 2
    left_indices = indices[:mid]
    right_indices = indices[mid:]
    if len(left_indices) > 0:
        _update_state(left_indices, curr_state, next_state, cache, apply_rule, r, t)
    if len(right_indices) > 0:
        _update_state(right_indices, curr_state, next_state, cache, apply_rule, r, t)


def _update_state(indices, curr_state, next_state, cache, apply_rule, r, t):
    """
     Perform an update on the given next state using the current state and memoization cache.

    :param indices: a list of the cell indices of the cells to update

    :param curr_state: the current state (i.e. the state after the previous timestep)

    :param next_state: the next state (i.e. the result after the current timestep)

    :param cache: a dictionary that maps state neighbourhoods to their activities

    :param apply_rule: the rule to apply during each cell update

    :param r: the neighbourhood radius

    :param t: the current timestep
    """
    # get the state string for the state given by the indices
    start = indices[0]
    end = indices[-1]
    neighbourhood_indices = range(start - r, end + 1 + r)
    neighbourhood = curr_state.take(neighbourhood_indices, mode='wrap')
    state_string = neighbourhood.tobytes()

    if state_string in cache:
        # update next_state with next vals from cache
        next_state[indices] = cache[state_string]
    else:
        if len(indices) > 1:
            _step(indices, curr_state, next_state, cache, apply_rule, r, t)
        else:
            # invoke rule and update next_state for cell
            val = apply_rule(neighbourhood, start, t)
            next_state[start] = val
        # get the result from the next_state for the left_indices and place in cache
        vals_to_cache = next_state[indices]
        cache[state_string] = vals_to_cache


def _get_memoized(n, c, t, apply_rule, memoization_table):
    """
    Checks if the result of `apply_rule` is in the memoization table according to the neighbourhood, `n`,
    and returns the associated value if it is. Otherwise, `apply_rule` is invoked and the result is stored in
    the memoization table, and then returned.

    :param n: a numpy array representing the neighbourhood

    :param c: an int representing the current cell's index

    :param t: an int, representing the current timestep

    :param apply_rule: a function representing the rule to be applied to each cell during the evolution; this function
                       will be given three arguments, in the following order: the neighbourhood, which is a numpy array
                       of length 2r + 1 representing the neighbourhood of the cell; the cell identity, which is a scalar
                       representing the index of the cell in the cellular automaton array; the time step, which is a
                       scalar representing the time step in the evolution

    :param memoization_table: a dictionary mapping a neighbourhood to the rule result for such a neighbourhood

    :return: the result of invoking the given rule with the given n, c, and t arguments
    """
    key = n.tobytes()
    if key in memoization_table:
        return memoization_table[key]
    else:
        result = apply_rule(n, c, t)
        memoization_table[key] = result
        return result


def _index_strides(arr, window_size):
    """
    Returns an array with dimensions len(cells) x window_size, representing the cell indices of the neighbourhood
    of each cell.

    :param arr: an array containing the cell indices; e.g. if there are 5 cells, then the argument
                will be [0, 1, 2, 3, 4]

    :param window_size: the size of the neighbourhood

    :return: an array with dimensions len(cells) x window_size, representing the cell indices of the neighbourhood
             of each cell
    """
    # this function is based on code in http://www.credid.io/cellular-automata-python-2.html
    arr = np.concatenate((arr[-window_size // 2 + 1:], arr, arr[:window_size // 2]))
    shape = arr.shape[:-1] + (arr.shape[-1] - window_size + 1, window_size)
    strides = arr.strides + (arr.strides[-1],)
    return np.lib.stride_tricks.as_strided(arr, shape=shape, strides=strides)


def bits_to_int(bits):
    """
    Converts a binary array representing a binary number into the corresponding int.

    :param bits: a list of 1s and 0s, representing a binary number

    :return: and int representing the corresponding number
    """
    total = 0
    for shift, j in enumerate(bits[::-1]):
        if j:
            total += 1 << shift
    return total


def int_to_bits(num, num_digits):
    """
    Converts the given number, `num`, to the corresponding binary number in the form of a NumPy array of 1s and 0s
    comprised of `num_digits` digits.

    :param num: the number, in base 10, to convert into binary

    :param num_digits: the number of digits the binary number should contain

    :return: a NumPy array of 1s and 0s representing the corresponding binary number
    """
    converted = list(map(int, bin(num)[2:]))
    return np.pad(converted, (num_digits - len(converted), 0), 'constant')


def binary_rule(neighbourhood, rule, scheme=None, powers_of_two=None):
    """
    Converts the given rule number to a binary representation, and uses this to determine the value to return.
    The process is approximately described as:

    .. code-block:: text

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

    :param rule: an int or a binary array indicating the cellular automaton rule number

    :param scheme: can be None (default) or 'nks'; if 'nks' is given, the rule numbering scheme used in NKS is used

    :param powers_of_two: a pre-computed array containing the powers of two, e.g. [4,2,1]; can be None (default) or an
                          array of length len(neighbourhood); if an array is given, it will used to speed up the
                          calculation of state_int

    :return: the result, 0 or 1, of applying the given rule on the given state
    """
    if powers_of_two is None:
        state_int = bits_to_int(neighbourhood)
    else:
        assert len(powers_of_two) == len(neighbourhood)
        state_int = neighbourhood.dot(powers_of_two)
    n = 2 ** len(neighbourhood)
    if isinstance(rule, (list, np.ndarray)):
        assert len(rule) == n
        rule_bin_array = rule
    else:
        rule_bin_array = int_to_bits(rule, n)
    if scheme == 'nks':
        return rule_bin_array[(n-1) - state_int]
    return rule_bin_array[state_int]


def nks_rule(neighbourhood, rule):
    """
    A convenience function, that calls binary_rule with scheme = 'nks'.

    :param neighbourhood: a binary array of length 2r + 1

    :param rule: an int indicating the cellular automaton rule number

    :return: the result, 0 or 1, of applying the given rule on the given state
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
        raise ValueError("rule number out of range")
    neighbourhood_sum = np.sum(neighbourhood)
    # the rightmost element of the rule is for the average color 0, in NKS convention
    return int(rule_string[n*(k - 1) - neighbourhood_sum], k)


def init_simple(size, val=1, dtype=np.int32):
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


def init_random(size, k=2, n_randomized=None, empty_value=0, dtype=np.int32):
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
        raise ValueError("the number of randomized sites, if specified, must be >= 0 and <= size")
    pad_left = (size - n_randomized) // 2
    pad_right = (size - n_randomized) - pad_left
    if np.issubdtype(dtype, np.integer):
        rand_nums = np.random.randint(k, size=n_randomized, dtype=dtype)
    else:
        rand_nums = np.random.uniform(0, k - 1, size=n_randomized).astype(dtype)
    return np.array([np.pad(np.array(rand_nums), (pad_left, pad_right), 'constant', constant_values=empty_value)])


def until_fixed_point():
    """
    Returns a callable to be used as the `timesteps` argument to the `evolve` and `evolve2d` functions, that will
    result in the evolution being halted when there have been no changes to the state of the CA in the
    last timestep. That is, if the last state of the CA is the same as the second-to-last state, the
    callable will return `False`, and evolution will be halted.

    :return: a callable to be used as the `timesteps` argument to the `evolve` and `evolve2d` functions
    """
    def _timesteps(ca, t):
        if len(ca) > 1:
            return False if (ca[-2] == ca[-1]).all() else True
        return True
    return _timesteps


class BaseRule:
    """
    A base rule class for custom rules to extend. A rule is a callable that accepts three parameters:
    1, the current cell's neighbourhood; 2, the index identifying the current cell; 3, an int identifying the
    current timestep. The rule returns the activity of the current cell at the next timestep.
    """
    def __call__(self, n, c, t):
        """
        The rule to be implemented by subclasses.

        :param n: the neighbourhood

        :param c: the index of the current cell

        :param t: the current timestep

        :return: the activity of the current cell at the next timestep
        """
        raise NotImplementedError


class NKSRule(BaseRule):
    """
    An Elementary Cellular Automaton rule, indexed according the scheme in NKS.
    """
    def __init__(self, nks_rule_number):
        """
        Creates an instance of an NKS rule.

        :param nks_rule_number: an int indicating the cellular automaton rule number
        """
        self._nks_rule_number = nks_rule_number

    def __call__(self, n, c, t):
        """
        The NKS rule to apply.

        :param n: a binary array of length 2r + 1

        :param c: the index of the current cell

        :param t: the current timestep

        :return: the result, 0 or 1, of applying the given rule on the given state
        """
        return nks_rule(n, self._nks_rule_number)


class BinaryRule(BaseRule):
    """
    A binary representation of the given rule number, which is used to determine the value to return.
    The process is approximately described as:

    .. code-block:: text

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
    """
    def __init__(self, rule, scheme=None, powers_of_two=None):
        """
        Creates an instance of a binary rule.

        :param rule: an int or a binary array indicating the cellular automaton rule number

        :param scheme: can be None (default) or 'nks'; if 'nks' is given, the rule numbering scheme used in NKS is used

        :param powers_of_two: a pre-computed array containing the powers of two, e.g. [4,2,1]; can be None (default) or
                              an array of length len(neighbourhood); if an array is given, it will used to speed up the
                              calculation of state_int
        """
        self._rule = rule
        self._scheme = scheme
        self._powers_of_two = powers_of_two

    def __call__(self, n, c, t):
        """
        The binary rule to apply.

        :param n: a binary array of length 2r + 1

        :param c: the index of the current cell

        :param t: the current timestep

        :return: the result, 0 or 1, of applying the given rule on the given state
        """
        return binary_rule(n, self._rule, self._scheme, self._powers_of_two)


class TotalisticRule(BaseRule):
    """
    The totalistic rule as described in NKS. The average color is mapped to a whole number in [0, k - 1].
    The rule number is in base 10, but interpreted in base k. For a 1-dimensional cellular automaton, there are
    3k - 2 possible average colors in the 3-cell neighbourhood. There are n(k - 1) + 1 possible average colors for a
    k-color cellular automaton with an n-cell neighbourhood.
    """
    def __init__(self, k, rule):
        """
        Creates an instance of a totalistic rule.

        :param k: the number of colors in this cellular automaton, where only 2 <= k <= 36 is supported

        :param rule: the k-color cellular automaton rule number in base 10, interpreted in base k
        """
        self._k = k
        self._rule = rule

    def __call__(self, n, c, t):
        """
        The totalistic rule to apply.

        :param n: a k-color array of any size

        :param c: the index of the current cell

        :param t: the current timestep

        :return: the result, a number from 0 to k - 1, of applying the given rule on the given state
        """
        return totalistic_rule(n, self._k, self._rule)


class ReversibleRule(BaseRule):
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

    def __call__(self, n, c, t):
        """
        The reversible rule to apply.

        :param n: the neighbourhood

        :param c: the index of the current cell

        :param t: the current timestep

        :return: the activity of the current cell at the next timestep
        """
        regular_result = nks_rule(n, self._rule_number)
        new_result = regular_result ^ self._previous_state[c]
        self._previous_state[c] = n[len(n) // 2]
        return new_result


class AsynchronousRule(BaseRule):
    """
    Creates an asynchronous cellular automaton rule with a cyclic update scheme. Also known as a sequential cellular
    automaton rule, in NKS. This rule wraps a given rule, making the given rule asynchronous. This rule works for 
    both 1D and 2D cellular automata.

    This rule requires the specification of an update order (if none is provided, then an order is constructed based
    on the number of cells in the CA). An update order specifies which cell will be updated as the CA evolves. For
    example, the update order [2, 3, 1] states that cell 2 will be updated in the next timestep, followed by cell 3 in
    the subsequent timestep, and then cell 1 in the timestep after that. This update order is adhered to for the
    entire evolution of the CA. Cells that are not being updated do not have the rule applied to them in that timestep.

    An option is provided to randomize the update order at the end of each cycle (i.e. timestep). This is equivalent to
    selecting a cell randomly at each timestep to update, leaving all others unchanged during that timestep.
    """
    def __init__(self, apply_rule, update_order=None, num_cells=None, randomize_each_cycle=False):
        """
        Constructs an asynchronous rule out of a given rule. Either the update_order or num_cells parameter must be
        specified. If no update_order is given, then the num_cells parameter must be specified, and an update order
        list will be constructed and shuffled.

        :param apply_rule: the rule that will be made asynchronous

        :param update_order: a list containing the indices of the cells in the CA, specifying the update order; if the
                             CA is 2D, then instead of indices, cell coordinates are expected (e.g. ((0,1), (2,3),...))

        :param num_cells: an int specifying the total number of cells in the CA if it is 1D, or a 2-tuple representing
                          the height and width of the CA if it is 2D

        :param randomize_each_cycle: whether to shuffle the update order list after each complete cycle
        """
        if update_order is None and num_cells is None:
            raise ValueError("either update_order or num_cells must be specified")
        self._apply_rule = apply_rule
        if update_order is not None:
            self._update_order = update_order
        else:
            self._init_update_order(num_cells)
            self._shuffle_update_order()
        self._curr = 0
        self._num_applied = 0
        self._randomize_each_cycle = randomize_each_cycle

    def _init_update_order(self, num_cells):
        if isinstance(num_cells, tuple):
            self._update_order = [(i, j) for i in range(num_cells[0]) for j in range(num_cells[1])]
        elif isinstance(num_cells, int):
            self._update_order = np.arange(num_cells)
        else:
            raise TypeError("num_cells must be either an int (1D CA) or a 2-tuple (2D CA)")

    def _shuffle_update_order(self):
        np.random.shuffle(self._update_order)

    def __call__(self, n, c, t):
        """
        The asynchronous rule to apply.

        :param n: the neighbourhood

        :param c: the index of the current cell

        :param t: the current timestep

        :return: the activity of the current cell at the next timestep
        """
        if self._in_update_order(c, n):
            self._num_applied += 1
        if not self._should_update(c, n):
            self._check_for_end_of_cycle()
            return self._current_cell_value(n)
        self._check_for_end_of_cycle()
        return self._apply_rule(n, c, t)

    def _in_update_order(self, c, n):
        return c in self._update_order

    def _should_update(self, c, n):
        return c == self._update_order[self._curr]

    def _check_for_end_of_cycle(self):
        if self._num_applied == len(self._update_order):
            self._curr = (self._curr + 1) % len(self._update_order)
            self._num_applied = 0
            if self._randomize_each_cycle:
                self._shuffle_update_order()

    def _current_cell_value(self, n):
        if len(n.shape) == 1:
            return n[len(n)//2]
        elif len(n.shape) == 2:
            return n[n.shape[0]//2][n.shape[1]//2]
        else:
            raise TypeError("unexpected neighbourhood dimensions: %s" % n.shape)
