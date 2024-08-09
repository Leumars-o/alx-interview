#!/usr/bin/python3
"""A module that returns the minimum number of operations
to reach a given number of characters.
"""


def prime_factors_list(num):
    """A function that returns a list of prime factors
    of a number.

    Args:
        num (int): A number to find prime factors for.

    Returns:
        list: A list of prime factors of a number.
    """
    factors = []
    div = 2

    while num > 1:
        if num % div == 0:
            factors.append(div)
            num //= div
        else:
            div += 1

    return factors


def minOperations(n):
    """A function that returns the minimum number of operations
    to reach a given number of characters.
    """

    factors = prime_factors_list(n)
    operations = 0

    for factor in factors:
        operations += factor

    return operations
