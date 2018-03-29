import cellpylib as ca
import numpy as np
import random

N = 200  # the number of cells
n_steps = 100  # the number of time steps in the simulation
r = 3  # the radius of the cell neighbourhood
threshold = 2  # the threshold to be reached in the cell's neighbourhood before it can have a chance to fire
rho = 0.15  # the probability that a cell fires spontaneously
phi = 0.6  # the probability that a cell fires if its threshold is reached
W = np.random.uniform(0, 1, (N, 2*r))  # initialize synaptic weights (probabilities) randomly, between 0 and 1

# cellular_automaton = ca.init_simple(N)
cellular_automaton = ca.init_random(N)

def left(state):
    return state[:len(state)//2]

def right(state):
    return state[len(state)//2+1:]

def rule1(state, c):
    cell_state = state[len(state)//2]
    total = np.sum(left(state)) + np.sum(right(state)) # activity of cells to the left and right of cell, not including cell itself
    if total >= threshold:
        if cell_state == 1:
            if random.random() > 0.65:
                return 0 #0 this is like a refractory period where the cell becomes quiet for a timestep if it was previously active
        return 1
    else:
        return 0

def rule2(state, c):
    if random.random() < rho:
        return 1
    total = np.sum(left(state)) + np.sum(right(state))
    if total >= threshold:
        if random.random() < phi:
            return 1
        return 0
    else:
        return 0

def rule3(state, c):
    if random.random() < rho:
        return 1
    weights = W[c]
    sum_left = sum(l for n, l in enumerate(left(state)) if random.random() < weights[n])
    sum_right = sum(r for n, r in enumerate(right(state)) if random.random() < weights[n + len(state)//2])
    total = sum_left + sum_right
    if total >= threshold and random.random() < phi:
        return 1
    return 0

"""
>>> s = np.array([0,1,1,0,1,0,1])
>>> s
array([0, 1, 1, 0, 1, 0, 1])
>>> W = np.random.uniform(0, 1, (1,6))
>>> W
array([[ 0.23996606,  0.56112597,  0.86498852,  0.6111952 ,  0.45682975, 0.98425582]])
>>> w = W[0]
>>> w
array([ 0.23996606,  0.56112597,  0.86498852,  0.6111952 ,  0.45682975, 0.98425582])
>>> left_prob_realized = np.array([int(random.random() < w[n]) for n, _ in enumerate(s[:len(s)//2])])
>>> left_prob_realized
array([1, 0, 1])
>>> left = s[:len(s)//2]
>>> left
array([0, 1, 1])
>>> left & left_prob_realized
array([0, 0, 1])
"""


# evolve the cellular automaton for n time steps
cellular_automaton = ca.evolve(cellular_automaton, n_steps=n_steps,
                               apply_rule=rule3, r=r)

ca.plot(cellular_automaton)
