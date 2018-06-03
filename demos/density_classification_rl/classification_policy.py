import tensorflow as tf
import numpy as np


class ClassificationPolicy:
    def __init__(self, n_input, n_hidden, n_output):
        self._sess = tf.Session()

        self._n_input = n_input
        self._n_hidden = n_hidden
        self._n_output = n_output

        self._input = tf.placeholder("float", [1, self._n_input], name="input")
        self._reward = tf.placeholder("float", (), name="reward")
        self._action_taken = tf.placeholder("float", [1, n_output], name="action_taken")
        self._learning_rate = tf.placeholder("float", (), "learning_rate")
        self._W_in = tf.Variable(tf.random_uniform([self._n_input, self._n_hidden], -1, 1), name="W_in")
        self._W_out = tf.Variable(tf.random_normal([self._n_hidden, self._n_output]), name="W_out")

        self._hidden_layer = tf.nn.tanh(tf.matmul(self._input, self._W_in))

        self._g = tf.nn.sigmoid(tf.matmul(self._hidden_layer, self._W_out))

        # self._log_g = tf.log(self._g)

        # self._loss = -self._log_g * self._reward # technically it's (reward - baseline), but we assume a zero baseline

        self._cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(
            logits=tf.matmul(self._hidden_layer, self._W_out), labels=self._action_taken)

        self._loss = self._cross_entropy * self._reward

        self._train_op = tf.train.GradientDescentOptimizer(self._learning_rate).minimize(self._loss)

        self._sess.run(tf.global_variables_initializer())

    def update(self, state, reward, action_taken, learning_rate):
        self._sess.run([self._train_op], feed_dict={
            self._input: state,
            self._reward: reward,
            self._action_taken: np.reshape(action_taken, [1, self._n_output]),
            self._learning_rate: learning_rate
        })

    def sample(self, state):
        probs = self._sess.run([self._g], feed_dict={self._input: state})
        probs = probs[0].tolist()[0]
        return np.random.binomial(1, p=probs)


# c = ClassificationPolicy()
# c.sample([[0, 1, 0, 1, 1]])