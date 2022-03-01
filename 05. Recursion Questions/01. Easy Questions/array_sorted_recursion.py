from typing import List

x = [1, 2, 3, 4, 5, 11, 7, 8]


def sorted(array: List, index: int) -> bool:
    if index == len(array) - 1:
        return True
    else:
        return array[index] <= array[index + 1] and sorted(array, index + 1)


print(sorted(x, 0))
