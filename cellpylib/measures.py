import math

import numpy as np


def shannon_entropy(string):
    """
    Calculates the Shannon entropy for the given string.
    :param string: any string, such as '000101001', '12402', or 'aBcd1234ef5g'
    :return: a real number representing the Shannon entropy
    """
    symbols = dict.fromkeys(list(string))
    symbol_probabilities = [float(string.count(symbol)) / len(string) for symbol in symbols]
    H = -sum([p_symbol * math.log(p_symbol, 2.0) for p_symbol in symbol_probabilities])
    return H + 0  # add 0 as a workaround so we don't end up with -0.0


def average_cell_entropy(cellular_automaton):
    """
    Calculates the average cell entropy in the given cellular automaton, where entropy is the Shannon entropy.
    In the case of a 1D cellular automaton, the state of a cell over time is represented as a string, and its entropy
     is calculated. The same is done for all cells in this cellular automaton, and the average entropy is returned.
    :param cellular_automaton: 
    :return: a real number representing the average cell Shannon entropy 
    """
    num_cols = cellular_automaton.shape[1]
    entropies = []
    for i in range(0, num_cols):
        cell_states_over_time = ''.join([str(x) for x in cellular_automaton[:, i]])
        entropy = shannon_entropy(cell_states_over_time)
        entropies.append(entropy)
    return np.mean(entropies)
