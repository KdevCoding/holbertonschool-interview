#!/usr/bin/python3
"""pascals triangle"""


def minOperations(n):
    """calcs fewest number of operations needed to result in exactly n H

    Args:
        n (int): count of letters wanted

    Returns:
        _type_: min operation needed
    """
    char = 1
    operations = 0
    clipboard = [0]
    i = 0
    while char < n:
        try:
            if clipboard[i] < char and (char * 2) <= n:
                clipboard.append(char)
                operations += 1
        except IndexError:
            pass
        for copy in reversed(clipboard):
            if (copy + char) <= n:
                char += copy
                operations += 1
                break
        i += 1
    return operations
