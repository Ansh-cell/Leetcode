class Solution:

    # https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

    def search(self, nums: List[int], target: int) -> bool:

        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False

        pivot_index = self.pivot(nums)
        if nums[pivot_index] == target:
            return True
        else:
            left_answer = self.binary_search(nums, target, 0, pivot_index - 1)
            if left_answer:
                return True
            else:
                return self.binary_search(nums, target, pivot_index + 1, len(nums) - 1)

    def pivot(self, arr):  # Time Complexity: O(n)
        start = 0
        end = len(arr) - 1

        while start < end:

            mid = start + (end - start) // 2

            if mid < end and arr[mid] > arr[mid + 1]:
                return mid
            elif mid > start and arr[mid] < arr[mid - 1]:
                return mid - 1
            elif arr[mid] == arr[start] and arr[mid] == arr[end]:
                if arr[start] > arr[start + 1]:
                    return start
                start += 1
                if arr[end] < arr[end - 1]:
                    return end - 1
                end -= 1
            elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[end] < arr[mid]):
                start = mid + 1
            else:
                end = mid - 1

        return end

    def binary_search(self, arr, target, start, end):  # Time Complexity: O(log(n))
        s = start
        e = end

        while s <= e:

            mid = s + (e - s) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return False
