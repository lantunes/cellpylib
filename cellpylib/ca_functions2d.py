from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def plot2d(ca, timestep=None, title=''):
    cmap = plt.get_cmap('Greys')
    plt.title(title)
    if timestep is not None:
        data = ca[timestep]
    else:
        data = ca[-1]
    plt.imshow(data, interpolation='none', cmap=cmap)
    plt.show()


def plot2d_slice(ca, slice=None, title=''):
    cmap = plt.get_cmap('Greys')
    plt.title(title)
    if slice is not None:
        data = ca[:, slice]
    else:
        data = ca[:, len(ca[0])//2]
    plt.imshow(data, interpolation='none', cmap=cmap)
    plt.show()


def plot2d_spacetime(ca, alpha=None, title=''):
    fig = plt.figure(figsize=(10, 7))
    plt.title(title)
    ax = fig.gca(projection='3d')
    ca = ca[::-1]
    xs = np.arange(ca.shape[2])[None, None, :]
    ys = np.arange(ca.shape[1])[None, :, None]
    zs = np.arange(ca.shape[0])[:, None, None]
    xs, ys, zs = np.broadcast_arrays(xs, ys, zs)
    masked_data = np.ma.masked_where(ca == 0, ca)
    ax.scatter(xs.ravel(),
               ys.ravel(),
               zs.ravel(),
               c=masked_data, cmap='cool', marker='s', depthshade=False, alpha=alpha, edgecolors='#0F0F0F')
    plt.show()


def evolve2d(cellular_automaton, timesteps, apply_rule, r=1, neighbourhood='Moore'):
    # """
    # >>> x
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])
    # >>> x[np.ix_([-1,0,1],[-1,0,1])]
    # array([[9, 7, 8],
    #        [3, 1, 2],
    #        [6, 4, 5]])
    # >>> x[np.ix_([-2,-1,0,1,2],[-2,-1,0,1,2])]
    # array([[5, 6, 4, 5, 6],
    #        [8, 9, 7, 8, 9],
    #        [2, 3, 1, 2, 3],
    #        [5, 6, 4, 5, 6],
    #        [8, 9, 7, 8, 9]])
    # >>> x[np.ix_([0,1,2],[0,1,2])]
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])
    # >>> x[np.ix_([0,1,2],[-1,0,1])]
    # array([[3, 1, 2],
    #        [6, 4, 5],
    #        [9, 7, 8]])
    # >>> x[np.ix_([-1,0,1],[0,1,2])]
    # array([[7, 8, 9],
    #        [1, 2, 3],
    #        [4, 5, 6]])
    #
    # :param cellular_automaton:
    # :param n_steps:
    # :param apply_rule:
    # :param r:
    # :param neighbourhood: the neighbourhood type; valid values are 'Moore', 9, 'von Neumann', and 5
    # :return:
    # """
    # _, rows, cols = cellular_automaton.shape
    # array = np.zeros((n_steps, rows, cols), dtype=np.int)
    # array[0] = cellular_automaton
    #
    # def index_strides(arr, window_size):
    #     # this function is based on code in http://www.credid.io/cellular-automata-python-2.html
    #     arr = np.concatenate((arr[-window_size//2+1:], arr, arr[:window_size//2]))
    #     shape = arr.shape[:-1] + (arr.shape[-1] - window_size + 1, window_size)
    #     strides = arr.strides + (arr.strides[-1],)
    #     return np.lib.stride_tricks.as_strided(arr, shape=shape, strides=strides)
    #
    # for i in range(1, n_steps):
    #     cell_layer = array[i - 1]
    #     strides = index_strides(np.arange(len(cell_layer)), 2*r + 1)
    #     states = cell_layer[strides]
    #     array[i] = np.array([apply_rule(s, c) for c, s in enumerate(states)])
    # return array
    pass  # TODO implement this


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
