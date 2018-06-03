import numpy as np

import cellpylib as cpl
from demos.density_classification_rl.classification_policy import ClassificationPolicy
import random
from random import randint


n_input = 149
n_ca_timesteps = 149
n_episodes = 100000
n_output = 128
n_hidden = 500
learning_rate = 0.05
n_trials = 100
epsilon = 0.5

policy = ClassificationPolicy(n_input=n_input, n_hidden=n_hidden, n_output=n_output)


def train(policy):
    noise = cpl.init_random(n_input)

    # ideal_rule = 6667021275756174439087127638698866559
    # rule_bits = policy.sample(noise) if episode_num % 2 == 0 else cpl.int_to_bits(ideal_rule, n_output)

    if random.random() < epsilon:
        rule_bits = [randint(0, 1) for b in range(1, n_output + 1)]
    else:
        rule_bits = policy.sample(noise)

    rule_number = cpl.bits_to_int(rule_bits)

    rewards = []
    for trial in range(n_trials):
        state = cpl.init_random(n_input)
        density_of_1s = np.count_nonzero(state) / n_input

        ca = cpl.evolve(state, timesteps=n_ca_timesteps,
                        apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_number), r=3)
        final_state = ca[-1]

        reward = 0
        if density_of_1s > 0.5:
            reward = np.sum(final_state) / n_input
            if np.count_nonzero(final_state) == n_input:
                reward += 1
        if density_of_1s < 0.5:
            reward = 1 - (np.sum(final_state) / n_input)
            if np.count_nonzero(final_state) == 0:
                reward += 1
        rewards.append(reward / n_trials)

    total_reward = np.sum(rewards)

    policy.update(noise, total_reward, rule_bits, learning_rate)

    return rule_number, total_reward


def evaluate(policy):
    noise = cpl.init_random(n_input)
    rule_bits = policy.sample(noise)
    rule_number = cpl.bits_to_int(rule_bits)
    num_correct = []
    for trial in range(10):
        state = cpl.init_random(n_input)
        density_of_1s = np.count_nonzero(state) / n_input

        ca = cpl.evolve(state, timesteps=n_ca_timesteps,
                        apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_number), r=3)
        final_state = ca[-1]

        reward = 0
        if density_of_1s > 0.5 and np.count_nonzero(final_state) == n_input:
            reward = 1
        if density_of_1s < 0.5 and np.count_nonzero(final_state) == 0:
            reward = 1
        num_correct.append(reward)
    total_correct = np.sum(num_correct)
    return rule_number, total_correct

for episode_num in range(1, n_episodes + 1):
    training_rule, training_reward = train(policy)
    eval_rule, eval_correct = evaluate(policy)

    print("episode: %s; training rule: %s; training reward: %s; eval rule: %s; total correct: %s" %
          (episode_num, training_rule, training_reward, eval_rule, eval_correct))