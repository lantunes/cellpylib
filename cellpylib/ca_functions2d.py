import numpy as np


def init_simple2d(rows, cols, val=1):
    """
    Returns a matrix initialized with zeroes, with its center value set to the specified value, or 1 by default.
    :param rows: the number of rows in the matrix
    :param cols: the number of columns in the matrix 
    :param val: the value to be used in the center of the matrix (1, by default)
    :return: a tensor with shape (1, rows, cols), with the center value initialized to the specified value, or 1 by default 
    """
    x = np.zeros((rows, cols), dtype=np.int)
    x[x.shape[0]//2][x.shape[1]//2] = val
    return np.array([x])


def init_random2d(rows, cols, k=2):
    """
    Returns a randomly initialized matrix with values consisting of numbers in {0,...,k - 1}, where k = 2 by default.
    :param rows: the number of rows in the matrix
    :param cols: the number of columns in the matrix 
    :param k: the number of states in the cellular automaton (2, by default)
    :return: a tensor with shape (1, rows, cols), randomly initialized with numbers in {0,...,k - 1}
    """
    return np.array([np.random.randint(k, size=(rows, cols), dtype=np.int)])
