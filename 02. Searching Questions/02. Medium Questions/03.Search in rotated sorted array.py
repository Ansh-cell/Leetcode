class Solution:

    # https://leetcode.com/problems/search-in-rotated-sorted-array/

    def search(self, nums: List[int], target: int) -> int:

        peak_element_index = self.peak_index(nums)
        if peak_element_index == -1:
            return self.binary_search(nums, target, 0, len(nums) - 1)
        elif nums[peak_element_index] == target:
            return peak_element_index
        else:
            search_left = self.binary_search(nums, target, 0, peak_element_index)
            if search_left != -1:
                return search_left
            else:
                search_right = self.binary_search(nums, target, peak_element_index + 1, len(nums) - 1)
                return search_right

    def peak_index(self, arr):

        start = 0
        end = len(arr) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if end > mid and arr[mid] > arr[mid + 1]:
                return mid
            elif start < mid and arr[mid] < arr[mid - 1]:
                return mid - 1
            elif arr[start] >= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def binary_search(self, arr, target, start, end):
        s = start
        e = end

        while s <= e:

            mid = s + (e - s) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return -1

    # Time Complexity: O(log(n)), Space Complexity: O(1)
