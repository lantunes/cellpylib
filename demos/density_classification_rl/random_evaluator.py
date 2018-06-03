import numpy as np
from random import randint
import cellpylib as cpl

n_input = 149
n_ca_timesteps = 149
n_output = 128
n_episodes = 100000

for episode_num in range(1, n_episodes + 1):
    state = cpl.init_random(n_input)
    density_of_1s = np.count_nonzero(state) / n_input

    rule_bits = [randint(0, 1) for b in range(1, n_output + 1)]
    rule_number = cpl.bits_to_int(rule_bits)

    ca = cpl.evolve(state, timesteps=n_ca_timesteps,
                    apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_number), r=3)
    final_state = ca[-1]

    reward = 0
    if density_of_1s > 0.5 and np.count_nonzero(final_state) == n_input:
        reward = 1
    if density_of_1s < 0.5 and np.count_nonzero(final_state) == 0:
        reward = 1

    print("episode: %s; density: %s; rule #: %s; reward: %s" % (episode_num, density_of_1s, rule_number, reward))