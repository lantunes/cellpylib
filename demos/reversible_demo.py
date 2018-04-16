import matplotlib.pyplot as plt
import numpy as np

import cellpylib as cpl


class ReversibleRule:
    def __init__(self, init_state, rule_number):
        self._previous_state = init_state
        self._rule_number = rule_number

    def apply_rule(self, n, c, t):
        regular_result = cpl.nks_rule(n, self._rule_number)
        new_result = regular_result ^ self._previous_state[c]
        self._previous_state[c] = n[len(n) // 2]
        return new_result

# NKS page 442
cellular_automaton = np.array([[0]*40 + [1]*20 + [0]*40])
r = ReversibleRule(cellular_automaton[0], 122)
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=1000,
                                apply_rule=r.apply_rule)

timestep = []
bientropies = []
shannon_entropies = []
apentropies = []
for i, c in enumerate(cellular_automaton):
    timestep.append(i)
    bit_string = ''.join([str(x) for x in c])
    bientropies.append(cpl.ktbien(bit_string))
    shannon_entropies.append(cpl.shannon_entropy(bit_string))
    apentropies.append(cpl.apen(bit_string, m=1, r=0))
    print("%s, %s, %s, %s" % (i, bientropies[-1], shannon_entropies[-1], apentropies[-1]))

plt.figure(1)
plt.title("KTBiEn")
plt.plot(timestep, bientropies)

plt.figure(2)
plt.title("Shannon Information")
plt.plot(timestep, shannon_entropies)

plt.figure(3)
plt.title("ApEn")
plt.plot(timestep, apentropies)

plt.figure(4)
cpl.plot(cellular_automaton)


