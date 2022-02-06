def findMin(nums):
    pivot_index = pivot(nums)
    return pivot_index
    # if pivot_index == len(nums) - 1:
    #     return nums[0]
    # else:
    #     return nums[pivot_index + 1]


def pivot(array):
    start = 0
    end = len(array) - 1

    while start < end:

        mid = start + (end - start) // 2

        if (array[mid] == array[start]) and (array[mid] == array[end]):

            if array[start] > array[start + 1]:
                return start
            start += 1

            if array[end] < array[end - 1]:
                return end - 1
            end -= 1

        elif array[start] < array[mid] or (array[start] == array[mid] and array[mid] > array[end]):

            start = mid + 1
        else:
            end = mid - 1

    return -1


x = [2, 2, 2, 0, 1]
print(findMin(x))
