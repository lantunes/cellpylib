import random

import numpy as np


def table_rule(state, table):
    """
    A rule where the state is converted into a string, and looked up in the given table, to yield the return value.
    :param state: a k-color array of length 2r + 1
    :param table: a table (map) of string representations of each neighbourhood state to the associated next 
           cell state value; for example, for k = 2 and r = 2, a valid table might be: 
           {'101': 1, '111': 0, '011': 0, '110': 1, '000': 0, '100': 0, '010': 0, '001': 1}
    :return: a number, from 0 to k - 1, associated with the given state as specified in the given table
    """
    state_repr = ''.join(str(x) for x in state)
    if not state_repr in table:
        raise Exception("could not find state '%s' in table" % state_repr)
    return table[state_repr]


def random_rule_table(k, r, lambda_val=None, quiescent_state=None, strong_quiescence=False, isotropic=False):
    """
    Constructs and returns a random rule table, as described in [Langton, C. G. (1990). Computation at the edge of 
    chaos: phase transitions and emergent computation. Physica D: Nonlinear Phenomena, 42(1-3), 12-37.], using 
    the "random-table" method.
    :param k: the number of cell states
    :param r: the radius of the cellular automaton neighbourhood
    :param lambda_val: a real number in (0., 1.), representing the value of lambda; if None, a default value of 
                       1.0 - 1/k will be used, where all states will be represented equally in the rule table
    :param quiescent_state: the state, a number in {0,...,k - 1}, to use as the quiescent state
    :param strong_quiescence: if True, all neighbourhood states uniform in cell state i will map to cell state i
    :param isotropic: if True, all planar rotations of a neighbourhood state will map to the same cell state
    :return: a tuple containing: a table describing a rule, constructed using the "random-table" table method as 
             described by C. G. Langton, the actual lambda value, and the quiescent state used
    """
    states = []
    n = 2*r + 1
    for i in range(0, k**n):
        states.append(np.base_repr(i, k).zfill(n))
    table = {}
    if lambda_val is None:
        lambda_val = 1. - (1. / k)
    if quiescent_state is None:
        quiescent_state = np.random.randint(k, dtype=np.int)
    if not (0 <= quiescent_state <= k - 1):
        raise Exception("quiescent state must be a number in {0,...,k - 1}")
    other_states = [x for x in range(0, k) if x != quiescent_state]
    quiescent_state_count = 0
    for state in states:
        if strong_quiescence and len(set(state)) == 1:
            # if the cell states in neighbourhood are all the same, e.g. '111'
            cell_state = int(state[0], k)
            if cell_state == quiescent_state: quiescent_state_count += 1
        else:
            state_reversed = state[::-1]
            if isotropic and state_reversed in table:
                cell_state = table[state_reversed]
                if cell_state == quiescent_state: quiescent_state_count += 1
            else:
                if random.random() < (1. - lambda_val):
                    cell_state = quiescent_state
                    quiescent_state_count += 1
                else:
                    cell_state = random.choice(other_states)
        table[state] = cell_state
    actual_lambda_val = (k**n - quiescent_state_count) / k**n
    return table, actual_lambda_val, quiescent_state


def table_walk_through(rule_table, lambda_val, k, r, quiescent_state, strong_quiescence=False, isotropic=False):
    """
    Perturbs the given rule table using the "table-walk-through" approach described in [Langton, C. G. (1990). 
    Computation at the edge of chaos: phase transitions and emergent computation. Physica D: Nonlinear Phenomena, 
    42(1-3), 12-37.]. The table's actual lambda value will be increased or decreased, incrementally and stochastically, 
    until it reaches the given lambda value.
    :param rule_table: a table (map) of string representations of each neighbourhood state to the associated next 
                       cell state value; for example, for k = 2 and r = 2, a valid table might be: 
                       {'101': 1, '111': 0, '011': 0, '110': 1, '000': 0, '100': 0, '010': 0, '001': 1}
    :param lambda_val: a real number in (0., 1.), representing the value of lambda
    :param k: the number of cell states
    :param r: the radius of the cellular automaton neighbourhood
    :param quiescent_state: the state, a number in {0,...,k - 1}, to use as the quiescent state
    :param strong_quiescence: if True, all neighbourhood states uniform in cell state i will map to cell state i
    :param isotropic: if True, all planar rotations of a neighbourhood state will map to the same cell state
    :return: a tuple containing: a table describing a rule, constructed using the "table-walk-through" method as 
             described by C. G. Langton, the actual lambda value
    """
    def actual_lambda():
        n = 2*r + 1
        transitions_to_quiescent_state = list(rule_table.values()).count(quiescent_state)
        return (k**n - transitions_to_quiescent_state) / k**n
    actual_lambda_val = actual_lambda()
    if actual_lambda_val == lambda_val:
        return rule_table, actual_lambda_val
    if actual_lambda_val > lambda_val:
        # reduce lambda
        attempts = 0
        while actual_lambda() > lambda_val and attempts < len(rule_table):
            attempts += 1
            states_to_others = [k for k in rule_table.keys() if rule_table[k] != quiescent_state]
            if strong_quiescence:
                # remove states that are all the same (i.e. '111'); presumably the strong quiescence condition is already
                #  enforced in the incoming rule table, and so these states shouldn't be changed
                states_to_others = [s for s in states_to_others if len(set(s)) != 1]
            if len(states_to_others) == 0:
                break
            state_to_perturb = random.choice(states_to_others)
            rule_table[state_to_perturb] = quiescent_state
            if isotropic:
                state_to_perturb_reversed = state_to_perturb[::-1]
                rule_table[state_to_perturb_reversed] = rule_table[state_to_perturb]
    elif actual_lambda_val < lambda_val:
        # increase lambda
        attempts = 0
        while actual_lambda() < lambda_val and attempts < len(rule_table):
            attempts += 1
            states_to_quiescent = [k for k in rule_table.keys() if rule_table[k] == quiescent_state]
            if strong_quiescence:
                # remove states that are all the same (i.e. '111')
                states_to_quiescent = [s for s in states_to_quiescent if len(set(s)) != 1]
            if len(states_to_quiescent) == 0:
                break
            state_to_perturb = random.choice(states_to_quiescent)
            other_states = [x for x in range(0, k) if x != quiescent_state]
            rule_table[state_to_perturb] = random.choice(other_states)
            if isotropic:
                state_to_perturb_reversed = state_to_perturb[::-1]
                rule_table[state_to_perturb_reversed] = rule_table[state_to_perturb]
    return rule_table, actual_lambda()
