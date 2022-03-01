from typing import *

x: List
x = [1, 2, 3, 5, 6, 5, 2, 9]
y = []


def search(array: List, index: int, target: int):
    if index == len(array) - 1:
        if array[index] == target:
            y.append(index)
            return
    else:
        if array[index] == target:
            y.append(index)
        return search(array, index + 1, target)


print(y)
