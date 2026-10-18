#!/usr/bin/python3
"""pascals triangle"""


def prime_factors(n):
    """find prime_factors

    Args:
        n (int): number to find factors of

    Returns:
        list: factors
    """
    factors = []
    div = 2

    while n >= 2:
        if n % div == 0:
            factors.append(div)
            n //= div
        else:
            div += 1

    return factors


def minOperations(n):
    """calcs fewest number of operations needed to result in exactly n H

    Args:
        n (int): count of letters wanted

    Returns:
        _type_: min operation needed
    """
    operations = 0

    if n != 0:
        for i in prime_factors(n):
            operations += i

    return operations
