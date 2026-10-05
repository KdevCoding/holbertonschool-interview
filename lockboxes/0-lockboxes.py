#!/usr/bin/python3

def canUnlockAll(boxes):
    keys= set()
    checking = True
    for loop in range(len(boxes) ** 2):
        for i, box in enumerate(boxes):
            if i in keys:
                for key in box:
                    keys.add(key)
    if len(keys) == len(boxes):
        ret = True
    else:
        ret = False
    return

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
