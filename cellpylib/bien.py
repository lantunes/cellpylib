import math

from .entropy import shannon_entropy


def binary_derivative(string):
    """
    Calculates the binary derivative of the given string, according to 
    Nathanson, M. B. (1971). Derivatives of binary sequences. SIAM Journal on Applied Mathematics, 21(3), 407-412
    :param string: a binary string, such as '110011' 
    :return: a binary string representing the binary derivative of the given string
    """
    result = []
    for i, d in enumerate(string):
        if i - 1 == len(string) - 2:
            break
        result.append(int(string[i]) ^ int(string[i + 1]))
    return ''.join([str(x) for x in result])


def bien(string):
    """
    Calculate the BiEntropy of the given string, according to 
    Croll, G. J. (2013). BiEntropy-The Approximate Entropy of a Finite Binary String. arXiv preprint arXiv:1305.0954.
    This version of BiEntropy is suitable for strings with length <= 32.
    :param string: a binary string, such as '110011'
    :return: a real number representing the BiEntropy of the given string
    """
    tot = 0.0
    n = len(string)
    for k in range(n - 1):
        tot += shannon_entropy(string) * 2**k
        string = binary_derivative(string)
    return (1 / (2**(n - 1) - 1)) * tot


def tbien(string):
    """
    Calculates the logarithmic weighting BiEntropy of the given string, according to
    Croll, G. J. (2013). BiEntropy-The Approximate Entropy of a Finite Binary String. arXiv preprint arXiv:1305.0954.
    This version of BiEntropy is suitable for strings with length > 32.
    :param string: a binary string, such as '110011'
    :return: a real number representing the logarithmic weighting BiEntropy of the given string
    """
    tot = 0.0
    tot_log = 0.0
    n = len(string)
    for k in range(n - 1):
        lg = math.log(k + 2, 2.0)
        tot += shannon_entropy(string) * lg
        tot_log += lg
        string = binary_derivative(string)
    return (1 / tot_log) * tot


def cyclic_binary_derivative(string):
    """
    Calculates the cyclic binary derivative, which is the "binary string of length n formed by XORing adjacent pairs of 
    digits including the last and the first." See:
    Croll, G. J. (2018). The BiEntropy of Some Knots on the Simple Cubic Lattice. arXiv preprint arXiv:1802.03772.
    :param string: a binary string, such as '110011' 
    :return: a binary string representing the cyclic binary derivative of the given string
    """
    result = []
    for i, d in enumerate(string):
        s = string[i]
        if i == len(string) - 1:
            next_s = string[0]
        else:
            next_s = string[i + 1]
        result.append(int(s) ^ int(next_s))
    return ''.join([str(x) for x in result])


def ktbien(string):
    """
    Calculates the knot logarithmic weighting BiEntropy of the given string, according to
    Croll, G. J. (2018). The BiEntropy of Some Knots on the Simple Cubic Lattice. arXiv preprint arXiv:1802.03772.
    :param string: a binary string, such as '110011'
    :return: a real number representing the knot logarithmic weighting BiEntropy of the given string
    """
    tot = 0.0
    tot_log = 0.0
    n = len(string)
    for k in range(n - 1):
        lg = math.log(k + 2, 2.0)
        tot += shannon_entropy(string) * lg
        tot_log += lg
        string = cyclic_binary_derivative(string)
    return (1 / tot_log) * tot
