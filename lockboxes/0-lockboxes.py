#!/usr/bin/python3
"""lockboxes
"""

def canUnlockAll(boxes):
    """check if all boxes can be opened

    Args:
        boxes (list of lists): boxes with keys

    Returns:
        bool: True if all boxes unlocked
    """

    keys = {0}
    while True:
        lenkey = len(keys)
        for i, box in enumerate(boxes):
            if i in keys:
                for key in box:
                    keys.add(key)
        if lenkey == len(keys):
            break
    return (lenkey >= len(boxes))


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [ [10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6] ]
    print(canUnlockAll(boxes))
