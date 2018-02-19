""" A random numbers generate module.
    Differents distributions are used in order to generate numbers.

    # Methods
    generate_uniform_random_number(low, high, size): generates a random number based on an uniform distribution.
    generate_gaussian_random_number(mean, variance, size): generates a random number based on a gaussian distribution.
"""

import numpy as np


def generate_uniform_random_number(low, high, size=1):
    """ Generates a random number based on an uniform distribution.

        # Arguments
            low: lower interval.
            high: higher interval.
            size: size of array.

        # Returns
            uniform_array: uniform random array.
    """
    uniform_array = np.random.uniform(low, high, size)
    return uniform_array


def generate_gaussian_random_number(mean, variance, size=1):
    """ Generates a random number based on a gaussian distribution.

        # Arguments
            mean: gaussian's mean value.
            variance: gaussian's variance value.
            size: size of array.

        # Returns
            gaussian_array: gaussian random array.
    """
    gaussian_array = np.random.normal(mean, variance, size)
    return gaussian_array
