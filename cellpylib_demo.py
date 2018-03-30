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
learning_rate = 0.05

# W = np.sort(W)
# W = np.flip(np.sort(W), 1)

# cellular_automaton = ca.init_simple(N)
cellular_automaton = ca.init_random(N)
# cellular_automaton = np.array([np.concatenate((np.ones(N//2, dtype=np.int), np.zeros(N//2, dtype=int)))])

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

def rule_learning(state, c):
    firing = 0
    if random.random() < rho:
        firing = 1
    weights = W[c]
    left_state = left(state)
    right_state = right(state)
    left_prob_realized = np.array([int(random.random() < weights[n]) for n, _ in enumerate(left_state)])
    right_prob_realized = np.array([int(random.random() < weights[n + len(state)//2]) for n, _ in enumerate(right_state)])
    total = sum(left_prob_realized & left_state) + sum(right_prob_realized & right_state)
    if firing != 1:
        if total >= threshold and random.random() < phi:
            firing = 1
    if firing != 0:
        # update the weights
        pos_weight_updates_left = (left_prob_realized & left_state) * learning_rate
        pos_weight_updates_right = (right_prob_realized & right_state) * learning_rate
        pos_weight_updates = np.concatenate((pos_weight_updates_left, pos_weight_updates_right))
        W[c] = np.clip(W[c] + pos_weight_updates, 0.05, 0.95)

        neg_weight_updates_left = (np.ones(len(left_state), dtype=np.int) - (left_prob_realized & left_state)) * learning_rate
        neg_weight_updates_right = (np.ones(len(right_state), dtype=np.int) - (right_prob_realized & right_state)) * learning_rate
        neg_weight_updates = np.concatenate((neg_weight_updates_left, neg_weight_updates_right))
        W[c] = np.clip(W[c] - neg_weight_updates, 0.05, 0.95)

    return firing

def rule_random(state, c):
    if random.random() < 0.5:
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

# r = 1
# n_steps = 100
# cellular_automaton = np.array([np.ones(N)])
# def stochastic_majority_voting(state, c):
#     tot = sum(state)
#     if tot > (len(state) / 2.) and random.random() < 0.9:
#         return 1
#     return 0


# evolve the cellular automaton for n time steps
cellular_automaton = ca.evolve(cellular_automaton, n_steps=n_steps,
                               apply_rule=rule3, r=r)

ca.plot(cellular_automaton)

# print(np.cov(cellular_automaton, rowvar=0))

# import matplotlib.pyplot as plt
# plt.imshow(np.cov(cellular_automaton, rowvar=0), interpolation='bilinear')
# plt.colorbar()
# plt.show()


"""
from https://www.cs.purdue.edu/homes/park/interest-ca.html

"A canonical problem concerns the reliability or (non)ergodicity of cellular automata, whose roots can be traced to 
von Neumann's study of fault-tolerant computation in Boolean circuits. In its simplest form, the CA reliability problem 
can be stated as a "memory" problem: can a deterministic CA remember its past when continually subject to noise? 

Example: "Can you remember a single bit?" Consider a 2-state one-dimensional CA implementing majority voting — a cell 
inspects the state of its two nearest neighbors and itself, and chooses as its next state the majority — where at each 
transition point a fault can occur with probability p. If a CA with an infinite number of cells (for finite CA the 
problem is trivial although the convergence rate is not) is started in a configuration where all cells are in state 1, 
will it continue to remember something about its initial configuration, or will faults collude and erase all memory of 
its beginning with the hands of time? Since the same CA can be started in a configuration where all cells are in 
state 0, one can advance the interpretation: can an infinite 1-D CA remember a single bit when immersed in a noisy 
environment? Here the meaning of remembering/storing is in its weakest form where we will grant retrieval of a single 
bit if the CA can correctly guess whence it came from with probability greater than 1/2."
- Kihong Park
"""