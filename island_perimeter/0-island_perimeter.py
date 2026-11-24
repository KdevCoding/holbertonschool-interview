#!/usr/bin/python3
"""island challenge"""


def island_perimeter(grid):
    """checks perimeter of island in given grid

    Args:
        grid (matrix): grid, 1 is island 0 is water

    Returns:
        int: perimeter
    """
    p = 0
    for len, row in enumerate(grid):
        for h, col in enumerate(row):
            i = 0
            if col == 1:
                try:
                    if grid[len - 1][h] == 1 and len != 0:
                        i += 1
                except IndexError:
                    pass
                try:
                    if grid[len + 1][h] == 1:
                        i += 1
                except IndexError:
                    pass
                try:
                    if grid[len][h - 1] == 1 and h != 0:
                        i += 1
                except IndexError:
                    pass
                try:
                    if grid[len][h + 1] == 1:
                        i += 1
                except IndexError:
                    pass
                p += 4 - i

    return p
