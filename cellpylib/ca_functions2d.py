from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.collections as mcoll
import numpy as np


def plot2d(ca, timestep=None, title='', *, colormap='Greys', show_grid=False, show_margin=True, scale=0.6,
           show=True, **imshow_kwargs):
    """
    Plots the state of the given 2D cellular automaton at the given timestep. If no timestep is provided, then the last
    timestep is plotted.

    The `show_margin` argument controls whether or not a margin is displayed in the resulting plot. When `show_margin`
    is set to `False`, then the plot takes up the entirety of the window. The `scale` argument is only used when the
    `show_margins` argument is `False`. It controls the resulting scale (i.e. relative size) of the image when there
    are no margins.

    :param ca: the 2D cellular automaton to plot

    :param timestep: the timestep of interest

    :param title: the title to place on the plot

    :param colormap: the color map to use (default is "Greys")

    :param show_grid: whether to display a grid (default is False)

    :param show_margin: whether to display the margin (default is True)

    :param scale: the scale of the figure (default is 0.6)

    :param show: show the plot (default is True)

    :param imshow_kwargs: keyword arguments for the Matplotlib `imshow` function
    """
    cmap = plt.get_cmap(colormap)
    fig, ax = plt.subplots()
    plt.title(title)
    if not show_margin:
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    if timestep is not None:
        data = ca[timestep]
    else:
        data = ca[-1]

    _add_grid_lines(ca, ax, show_grid)

    im = plt.imshow(data, interpolation='none', cmap=cmap, **imshow_kwargs)
    if not show_margin:
        baseheight, basewidth = im.get_size()
        fig.set_size_inches(basewidth*scale, baseheight*scale, forward=True)
    if show:
        plt.show()


def plot2d_slice(ca, slice=None, title='', *, colormap='Greys', show_grid=False, show_margin=True, scale=0.6,
                 show=True, **imshow_kwargs):
    """
    Plots a slice through the evolved states of a 2D cellular automaton. For example, consider the following `ca`,
    which may represent the evolution of a 3x3 2D cellular automaton over 3 timesteps:

    .. code-block:: text

        [[[ 1,  2,  3],
          [ 4,  5,  6],
          [ 7,  8,  9]],
         [[10, 11, 12],
          [13, 14, 15],
          [16, 17, 18]],
         [[19, 20, 21],
          [22, 23, 24],
          [25, 26, 27]]]

    By default, the following would be plotted:

    .. code-block:: text

        [[ 4,  5,  6],
         [13, 14, 15],
         [22, 23, 24]]

    If `0` is provided as the `slice` argument, then the following would be plotted:

    .. code-block:: text

        [[ 1,  2,  3],
         [10, 11, 12],
         [19, 20, 21]]

    The `show_margin` argument controls whether or not a margin is displayed in the resulting plot. When `show_margin`
    is set to `False`, then the plot takes up the entirety of the window. The `scale` argument is only used when the
    `show_margins` argument is `False`. It controls the resulting scale (i.e. relative size) of the image when there
    are no margins.

    :param ca: the 2D cellular automaton to plot

    :param slice: an int representing the index of the row to plot; by default, the "center" row is used

    :param title: the title to place on the plot

    :param colormap: the color map to use (default is "Greys")

    :param show_grid: whether to display a grid (default is False)

    :param show_margin: whether to display the margin (default is True)

    :param scale: the scale of the figure (default is 0.6)

    :param show: show the plot (default is True)

    :param imshow_kwargs: keyword arguments for the Matplotlib `imshow` function
    """
    cmap = plt.get_cmap(colormap)
    fig, ax = plt.subplots()
    plt.title(title)
    if not show_margin:
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    if slice is not None:
        data = ca[:, slice]
    else:
        data = ca[:, len(ca[0])//2]

    _add_grid_lines(ca, ax, show_grid)

    im = plt.imshow(data, interpolation='none', cmap=cmap, **imshow_kwargs)
    if not show_margin:
        baseheight, basewidth = im.get_size()
        fig.set_size_inches(basewidth*scale, baseheight*scale, forward=True)
    if show:
        plt.show()


def plot2d_spacetime(ca, alpha=None, title='', show=True):
    """
    Plots the evolution of the given 2D cellular automaton as a 3D space-time plot.

    :param ca: the 2D cellular automaton to plot

    :param alpha: the alpha blending value; a real number between 0 (transparent) and 1 (opaque)

    :param title: the title to place on the plot

    :param show: show the plot (default is True)
    """
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
               c=masked_data.ravel(), cmap='cool', marker='s', depthshade=False, alpha=alpha, edgecolors='#0F0F0F')
    if show:
        plt.show()


def plot2d_animate(ca, title='', *, colormap='Greys', show_grid=False, show_margin=True, scale=0.6, dpi=80,
                   interval=50, save=False, autoscale=False, show=True, **imshow_kwargs):
    """
    Animate the given 2D cellular automaton.

    The `show_margin` argument controls whether or not a margin is displayed in the resulting plot. When `show_margin`
    is set to `False`, then the plot takes up the entirety of the window. The `scale` argument is only used when the
    `show_margins` argument is `False`. It controls the resulting scale (i.e. relative size) of the image when there
    are no margins.

    The `dpi` argument represents the dots per inch of the animation when it is saved. There will be no visible effect
    of the `dpi` argument if the animation is not saved (i.e. when `save` is `False`).

    :param ca:  the 2D cellular automaton to animate

    :param title: the title to place on the plot (default is "")

    :param colormap: the color map to use (default is "Greys")

    :param show_grid: whether to display a grid (default is False)

    :param show_margin: whether to display the margin (default is True)

    :param scale: the scale of the figure (default is 0.6)

    :param dpi: the dots per inch of the image (default is 80)

    :param interval: the delay between frames in milliseconds (default is 50)

    :param save: whether to save the animation to a local file (default is False)

    :param autoscale: whether to autoscale the images in the animation; this should be set to True if the first
                      frame has a uniform value (e.g. all zeroes) (default is False)

    :param show: show the plot (default is True)

    :param imshow_kwargs: keyword arguments for the Matplotlib `imshow` function
    """
    cmap = plt.get_cmap(colormap)
    fig, ax = plt.subplots()
    plt.title(title)
    if not show_margin:
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

    grid = _add_grid_lines(ca, ax, show_grid)

    im = plt.imshow(ca[0], animated=True, cmap=cmap, **imshow_kwargs)
    if not show_margin:
        baseheight, basewidth = im.get_size()
        fig.set_size_inches(basewidth*scale, baseheight*scale, forward=True)

    i = {'index': 0}
    def updatefig(*args):
        i['index'] += 1
        if i['index'] == len(ca):
            i['index'] = 0
        im.set_array(ca[i['index']])
        if autoscale:
            im.autoscale()
        return im, grid
    ani = animation.FuncAnimation(fig, updatefig, interval=interval, blit=True, save_count=len(ca))
    if save:
        ani.save('evolved.gif', dpi=dpi, writer="imagemagick")
    if show:
        plt.show()


def _add_grid_lines(ca, ax, show_grid):
    """
    Adds grid lines to the plot.

    :param ca: the 2D cellular automaton to plot

    :param ax: the Matplotlib axis object

    :param show_grid: whether to display the grid lines

    :return: the grid object
    """
    grid_linewidth = 0.0
    if show_grid:
        plt.xticks(np.arange(-.5, len(ca[0][0]), 1), "")
        plt.yticks(np.arange(-.5, len(ca[0]), 1), "")
        plt.tick_params(axis='both', which='both', length=0)
        grid_linewidth = 0.5
    vertical = np.arange(-.5, len(ca[0][0]), 1)
    horizontal = np.arange(-.5, len(ca[0]), 1)
    lines = ([[(x, y) for y in (-.5, horizontal[-1])] for x in vertical] +
             [[(x, y) for x in (-.5, vertical[-1])] for y in horizontal])
    grid = mcoll.LineCollection(lines, linestyles='-', linewidths=grid_linewidth, color='grey')
    ax.add_collection(grid)

    return grid


def evolve2d(cellular_automaton, timesteps, apply_rule, r=1, neighbourhood='Moore'):
    """
    Evolves the given cellular automaton for the specified time steps. Applies the given function to each cell during
    the evolution. A cellular automaton is represented here as an array of arrays, or matrix. This function expects
    an array containing the initial time step (i.e. initial condition, an array) for the cellular automaton. The final
    result is a matrix, where the number of rows equal the number of time steps specified.

    :param cellular_automaton: the cellular automaton starting condition representing the first time step

    :param timesteps: the number of time steps in this evolution; note that this value refers to the total number of
                      time steps in this cellular automaton evolution, which includes the initial condition

    :param apply_rule: a function representing the rule to be applied to each cell during the evolution; this function
                       will be given three arguments, in the following order: the neighbourhood, which is a numpy
                       2D array of dimensions 2r+1 x 2r+1, representing the neighbourhood of the cell (if the
                       'von Neumann' neighbourhood is specified, the array will be a masked array); the cell identity,
                       which is a tuple representing the row and column indices of the cell in the cellular automaton
                       matrix, as (row, col); the time step, which is a scalar representing the time step in the
                       evolution

    :param r: the neighbourhood radius; the neighbourhood dimensions will be 2r+1 x 2r+1

    :param neighbourhood: the neighbourhood type; valid values are 'Moore' or 'von Neumann'

    :return: a list of matrices, containing the results of the evolution, where the number of rows equal the number
             of time steps specified
    """
    _, rows, cols = cellular_automaton.shape
    array = np.zeros((timesteps, rows, cols), dtype=cellular_automaton.dtype)
    array[0] = cellular_automaton

    von_neumann_mask = np.zeros((2*r + 1, 2*r + 1), dtype=bool)
    for i in range(len(von_neumann_mask)):
        mask_size = np.absolute(r - i)
        von_neumann_mask[i][:mask_size] = 1
        if mask_size != 0:
            von_neumann_mask[i][-mask_size:] = 1

    def get_neighbourhood(cell_layer, row, col):
        row_indices = range(row - r, row + r + 1)
        row_indices = [i - cell_layer.shape[0] if i > (cell_layer.shape[0] - 1) else i for i in row_indices]
        col_indices = range(col - r, col + r + 1)
        col_indices = [i - cell_layer.shape[1] if i > (cell_layer.shape[1] - 1) else i for i in col_indices]
        n = cell_layer[np.ix_(row_indices, col_indices)]
        if neighbourhood == 'Moore':
            return n
        elif neighbourhood == 'von Neumann':
            return np.ma.masked_array(n, von_neumann_mask)
        else:
            raise Exception("unknown neighbourhood type: %s" % neighbourhood)

    for t in range(1, timesteps):
        cell_layer = array[t - 1]
        for row, cell_row in enumerate(cell_layer):
            for col, cell in enumerate(cell_row):
                n = get_neighbourhood(cell_layer, row, col)
                array[t][row][col] = apply_rule(n, (row, col), t)
    return array


def init_simple2d(rows, cols, val=1, dtype=np.int32, coords=None):
    """
    Returns a matrix initialized with zeroes, with its center value set to the specified value, or 1 by default.
    If the `coords` argument is specified, then the specified cell at the given coordinates will have its value
    set to `val`, otherwise the center cell will be set.

    :param rows: the number of rows in the matrix

    :param cols: the number of columns in the matrix

    :param val: the value to be used in the center of the matrix (1, by default)

    :param dtype: the data type (np.int32 by default)

    :param coords: a 2-tuple specifying the row and column of the cell to be initialized (None by default)

    :return: a tensor with shape (1, rows, cols), with the center value initialized to the specified value, or 1 by default
    """
    x = np.zeros((rows, cols), dtype=dtype)
    if coords is not None:
        if not isinstance(coords, (tuple, list)) or len(coords) != 2:
            raise Exception("coords must be a list or tuple of length 2")
        x[coords[0]][coords[1]] = val
    else:
        x[x.shape[0]//2][x.shape[1]//2] = val
    return np.array([x])


def init_random2d(rows, cols, k=2, dtype=np.int32):
    """
    Returns a randomly initialized matrix with values consisting of numbers in {0,...,k - 1}, where k = 2 by default.
    If dtype is not an integer type, then values will be uniformly distributed over the half-open interval [0, k - 1).

    :param rows: the number of rows in the matrix

    :param cols: the number of columns in the matrix

    :param k: the number of states in the cellular automaton (2, by default)

    :param dtype: the data type

    :return: a tensor with shape (1, rows, cols), randomly initialized with numbers in {0,...,k - 1}
    """
    if np.issubdtype(dtype, np.integer):
        rand_nums = np.random.randint(k, size=(rows, cols), dtype=dtype)
    else:
        rand_nums = np.random.uniform(0, k - 1, size=(rows, cols)).astype(dtype)
    return np.array([rand_nums])


def game_of_life_rule(neighbourhood, c, t):
    """
    Conway's Game of Life rule.

    :param neighbourhood: the current cell's neighbourhood

    :param c: the index of the current cell

    :param t: the current timestep

    :return: the state of the current cell at the next timestep
    """
    center_cell = neighbourhood[1][1]
    total = np.sum(neighbourhood)
    if center_cell == 1:
        if total - 1 < 2:
            return 0  # Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
        if total - 1 == 2 or total - 1 == 3:
            return 1  # Any live cell with two or three live neighbours lives on to the next generation.
        if total - 1 > 3:
            return 0  # Any live cell with more than three live neighbours dies, as if by overpopulation.
    else:
        if total == 3:
            return 1  # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        else:
            return 0
