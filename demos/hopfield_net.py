import numpy as np
import cellpylib as cpl


"""
Based on: http://neupy.com/2015/09/20/discrete_hopfield_network.html
"""
# patterns for training
zero = [
     0, 1, 1, 1, 0,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     0, 1, 1, 1, 0,
     0, 0, 0, 0, 0] # we add this last row so that we get an odd number of
                    #  total cells, so that we can specify a radius that includes exactly all the cells
one = [
     0, 1, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 0, 0, 0]

two = [
     1, 1, 1, 0, 0,
     0, 0, 0, 1, 0,
     0, 0, 0, 1, 0,
     0, 1, 1, 0, 0,
     1, 0, 0, 0, 0,
     1, 1, 1, 1, 1,
     0, 0, 0, 0, 0]
# replace the zeroes with -1 to make these vectors bipolar instead of binary
one = [-1 if x == 0 else x for x in one]
two = [-1 if x == 0 else x for x in two]
zero = [-1 if x == 0 else x for x in zero]

P = [zero, one, two]
r = 17 # TODO we need to implement the adjancency matrix, so that we aren't restricted to an odd number of total cells

# patterns to evaluate
half_zero = [
     0, 1, 1, 1, 0,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0]

half_one = [
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0]

half_two = [
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 1, 1, 0, 0,
     1, 0, 0, 0, 0,
     1, 1, 1, 1, 1,
     0, 0, 0, 0, 0]
half_zero = [-1 if x == 0 else x for x in half_zero]
half_one = [-1 if x == 0 else x for x in half_one]
half_two = [-1 if x == 0 else x for x in half_two]

cellular_automaton = np.array([half_zero])


# weights / training step; the patterns should be composed of bipolar ({-1,1}) and not binary ({0,1}) values
# TODO the W and apply_rule below could all be encapsulated in a HopfieldNet class;
#   the class would have a train() method and the apply_rule() method
W = np.zeros((len(P[0]), len(P[0])), dtype=np.int)
for p in P:
    for i in range(len(p)):
        for j in range(len(p)):
            if i ==j:
                W[i, j] = 0
            else:
                W[i, j] += p[i]*p[j]

# an asynchronous cellular automaton with a cyclic update scheme
update_order = np.arange(len(cellular_automaton[0]))
np.random.shuffle(update_order)
update_order = update_order.tolist()
curr = 0
def apply_rule(n, c, t):
    global update_order
    global curr
    if c != update_order[curr]:
        if c == len(n) - 1:
            curr = (curr + 1) % len(update_order)
        return n[len(n)//2]  # the current state of the cell
    if c == len(n) - 1:
        curr = (curr + 1) % len(update_order)

    left_neighbours = n[0 : len(n)//2]
    right_neighbours = n[len(n)//2 + 1 :]
    V = 0
    for j, left_V in enumerate(left_neighbours):
        V += W[c - r + j, c] * left_V
    for j, right_V in enumerate(right_neighbours):
        V += W[(c + j + 1) % len(n), c] * right_V
    return 1 if V >= 0 else -1

cellular_automaton = cpl.evolve(cellular_automaton, 155, apply_rule=apply_rule, r=r)

cpl.plot(W)
cpl.plot2d_animate(np.reshape(cellular_automaton, (155, 7,5)))