# import cellpylib as ca
# import numpy as np
#
# cellular_automaton = ca.init_random(149)
#
# print("density of 1s: %s" % (np.count_nonzero(cellular_automaton) / 149))
#
# # M. Mitchell et al. discovered this rule using a Genetic Algorithm
# rule_number = 6667021275756174439087127638698866559
#
# cellular_automaton = ca.evolve(cellular_automaton, n_steps=149,
#                                apply_rule=lambda state: ca.number_rule(state, rule_number), r=3)
#
# ca.plot(cellular_automaton)


import math


def shannon_entropy(string):
    symbols = dict.fromkeys(list(string))
    symbol_probabilities = [float(string.count(symbol)) / len(string) for symbol in symbols]
    H = -sum([p_symbol * math.log(p_symbol, 2.0) for p_symbol in symbol_probabilities])
    return H + 0  # add 0 as a workaround so we don't end up with -0.0


s = "00000000000000" # 0.0
print("shannon: %s: %s" % (s, shannon_entropy(s)))
s = "11111111111111" # 0.0
print("shannon: %s: %s" % (s, shannon_entropy(s)))
s = "01010001001010" # 0.9402859586706309
print("shannon: %s: %s" % (s, shannon_entropy(s)))
s = "11011011001110" # 0.9402859586706309
print("shannon: %s: %s" % (s, shannon_entropy(s)))
s = "10000001000000" # 0.5916727785823274
print("shannon: %s: %s" % (s, shannon_entropy(s)))
s = "10101010101010" # this string has a high Shannon entropy (1.0), but it displays a lot of regularity
print("shannon: %s: %s" % (s, shannon_entropy(s)))
s = "11111110000000" # 1.0
print("shannon: %s: %s" % (s, shannon_entropy(s)))

from bitstring import Bits
from bientropy import bien

s = "00000000000000"
print("bien: %s: %s" % (s, bien(Bits(bin=s))))
s = "11111111111111"
print("bien: %s: %s" % (s, bien(Bits(bin=s))))
s = "01010001001010"
print("bien: %s: %s" % (s, bien(Bits(bin=s))))
s = "11011011001110"
print("bien: %s: %s" % (s, bien(Bits(bin=s))))
s = "10000001000000"
print("bien: %s: %s" % (s, bien(Bits(bin=s))))
s = "10101010101010"
print("bien: %s: %s" % (s, bien(Bits(bin=s))))
s = "11111110000000"
print("bien: %s: %s" % (s, bien(Bits(bin=s))))

s = "1011"
print("bien: %s: %s" % (s, bien(Bits(bin=s))))
s = "1001"
print("bien: %s: %s" % (s, bien(Bits(bin=s))))
s = "00000001"
print("bien: %s: %s" % (s, bien(Bits(bin=s))))

bins = {'0.1':0,'0.2':0, '0.3':0, '0.4':0, '0.5':0, '0.6':0, '0.7':0, '0.8':0, '0.9':0, '1.0':0}

# rule 30
for r in range(0, 256):
    s = format(r, '08b')
    b = bien(Bits(bin=s))
    print("rule %s bien: %s: %s" % (r, s, b))
    if b >= 0 and b < 0.1:
        bins['0.1'] += 1
    elif b >= 0.1 and b < 0.2:
        bins['0.2'] += 1
    elif b >= 0.2 and b < 0.3:
        bins['0.3'] += 1
    elif b >= 0.3 and b < 0.4:
        bins['0.4'] += 1
    elif b >= 0.4 and b < 0.5:
        bins['0.5'] += 1
    elif b >= 0.5 and b < 0.6:
        bins['0.6'] += 1
    elif b >= 0.6 and b < 0.7:
        bins['0.7'] += 1
    elif b >= 0.7 and b < 0.8:
        bins['0.8'] += 1
    elif b >= 0.8 and b < 0.9:
        bins['0.8'] += 1
    elif b >= 0.9 and b < 1.0:
        bins['1.0'] += 1

print(bins)

"""
'1.0': 128, 
'0.9': 0
'0.8': 0, 
'0.7': 0, 
'0.6': 0, 
'0.5': 64, 
'0.4': 0, 
'0.3': 32, 
'0.2': 16, 
'0.1': 16, 
"""


# Boltzmann's entropy is expressed as: S = k ln W, where k is Boltzmann's constant (irrelevant in information theory)
# and W is the number of microstates. His assumption is that each microstate has an equal probability of
# being occupied. The kind of system Boltzmann imagined was something like "11111110000000" or "10101010101010", where
# here there are only two microstates: "1" and "0". The string "11111110000000" is a macrostate, one of 16,384 (2^14)
# macrostates (as the string has a length of 14), though we are only interested in those with equal number of 1s and 0s.
# Systems which have an equal probability of being in each microstate are said to be in equilibrium.
# Note that in physics, ln (log with base e) is common, whereas in computer science, log with base 2 is common. So, in
# the system of binary strings of length 14, where each microstate has an equal probability of occurrence, then the
# entropy H is log[base 2] 2, or 1. This is indeed the same value we get using the Shannon entropy:
# H = -Sum[each microstate i] p[i] * log[base 2] p[i], if there are two microstates and each has a probability of 0.5.
#
# Shannon entropy is expressed as: H = -Sum[each microstate i] p[i] * log[base 2] p[i]. This related in form to the
# Gibbs entropy: S = -k Sum[each microstate i] p[i] * ln p[i]. The motivation for these forms of entropy is that
# the probabilities of microstates being occupied are not equal. The kind of system that Gibbs imagined is something
# like "10000001000000". Again, here, there are two microstates, "1" and "0". Non-equilibrium systems have unequal
# probabilities of being in various microstates.
#
# The question is whether a string like "10101010101010" should have a high or low entropy. The definition of what a
# symbol is depends on the alphabet. A source that always generates the same symbol has an entropy of 0. A source that
# generates each symbol with equal probability has an entropy of 1. Shannon was considering the problem of information
# transmission. So each binary digit, "1" and "0", are the symbols in question. However, if we consider "10" to be the
# symbol in question (one of possible microstates "11", "00", "10", "01"), then the string "10101010101010" has an
# entropy of 0.

# What are the BiEntropies of the 8-bit CA rules studied by Wolfram? Is there a correlation between their BiEntropy
# and their rule class (i.e. 1, 2, 3 or 4)?
