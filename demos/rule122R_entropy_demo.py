import matplotlib.pyplot as plt
import numpy as np

import cellpylib as cpl

# NKS page 442 - Rule 122R
cellular_automaton = np.array([[0]*40 + [1]*20 + [0]*40])
r = cpl.ReversibleRule(cellular_automaton[0], 122)
cellular_automaton = cpl.evolve(cellular_automaton, timesteps=1000, apply_rule=r.apply_rule)

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


