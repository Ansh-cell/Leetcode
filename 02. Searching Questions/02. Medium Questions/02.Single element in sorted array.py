class Solution:

    # https://leetcode.com/problems/single-element-in-a-sorted-array/

    def singleNonDuplicate(self, nums: List[int]) -> int:

        return self.search_single_element(nums)

    def search_single_element(self, arr):
        start = 0
        end = len(arr) - 1

        if len(arr) == 1:       # If the length of the array is 1
            return arr[0]

        while start <= end:

            mid = start + (end - start) // 2
            if mid == 0 or mid == len(arr) - 1:     # if the answer lies at the start or end of the list
                return arr[mid]
            elif arr[mid - 1] != arr[mid] and arr[mid + 1] != arr[mid]:  # if the answer is mid
                return arr[mid]
            elif arr[mid - 1] == arr[mid]:  # if the answer lies on the left
                if (mid - 1) % 2 != 0:
                    end = mid - 2
                else:
                    start = mid + 1
            elif arr[mid + 1] == arr[mid]:      # if the answer lies on right side
                if (len(arr) - 2 - mid) % 2 != 0:
                    start = mid + 2
                else:
                    end = mid - 1

    # Time Complexity: O(log(n)), Space Complexity: O(1)
