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
    :param cellular_automaton: the cellular automaton to perform this operation on
    :return: a real number representing the average cell Shannon entropy 
    """
    num_cols = cellular_automaton.shape[1]
    entropies = []
    for i in range(0, num_cols):
        cell_states_over_time = ''.join([str(x) for x in cellular_automaton[:, i]])
        entropy = shannon_entropy(cell_states_over_time)
        entropies.append(entropy)
    return np.mean(entropies)


def joint_shannon_entropy(stringX, stringY):
    """
    Calculates the joint Shannon entropy between the given strings, which must be of the same length.
    :param stringX: any string, such as '000101001', '12402', or 'aBcd1234ef5g'
    :param stringY: any string, such as '000101001', '12402', or 'aBcd1234ef5g' 
    :return: a real number representing the joint Shannon entropy between the given strings
    """
    X = np.array(list(stringX))
    Y = np.array(list(stringY))
    joint_symbol_probabilities = []
    for x in set(X):
        for y in set(Y):
            joint_symbol_probabilities.append(np.mean(np.logical_and(X == x, Y == y)))
    return np.sum(-p * np.log2(p) for p in joint_symbol_probabilities if p != 0)


def mutual_information(stringX, stringY):
    """
    Calculates the mutual information between the given strings, which must be of the same length.
    :param stringX: any string, such as '000101001', '12402', or 'aBcd1234ef5g'
    :param stringY: any string, such as '000101001', '12402', or 'aBcd1234ef5g'
    :return: a real number representing the mutual information between the given strings
    """
    return shannon_entropy(stringX) + shannon_entropy(stringY) - joint_shannon_entropy(stringX, stringY)


def average_mutual_information(cellular_automaton, temporal_distance=1):
    """
    Calculates the average mutual information between a cell and itself at the next n time steps, given by the 
    specified temporal distance. A temporal distance of 1 means the next time step.
    For example, consider the following string, '00101010110', which represents the state of a cell over 11 time steps.
     The strings which will be used for the computation of the mutual information between a cell and itself at the 
     next time step are: '0010101011' and '0101010110', since we pair each time-step value with its next value:
     " 00101010110"
     "00101010110 "
    :param cellular_automaton: the cellular automaton to perform this operation on
    :param temporal_distance: the size of temporal separation, where the value must be greater than 0 and
                              less than the number of time steps.
    :return: a real number representing the average mutual information between a cell and itself at the next time step
    """
    num_cols = cellular_automaton.shape[1]
    if not (0 < temporal_distance < num_cols):
        raise Exception("the temporal distance must be greater than 0 and less than the number of time steps")
    mutual_informations = []
    for i in range(0, num_cols):
        cell_states_over_time = ''.join([str(x) for x in cellular_automaton[:, i]])
        mi = mutual_information(cell_states_over_time[:-temporal_distance], cell_states_over_time[temporal_distance:])
        mutual_informations.append(mi)
    return np.mean(mutual_informations)
