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
    checking = True
    for loop in range((len(boxes) ** 2) // 2):
        for i, box in enumerate(boxes):
            if i in keys:
                for key in box:
                    keys.add(key)
    return (len(keys) == len(boxes))
