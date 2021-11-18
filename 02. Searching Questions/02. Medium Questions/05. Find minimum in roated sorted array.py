class Solution:

    # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

    def findMin(self, nums: List[int]) -> int:

        answer = self.peak_element(nums)
        if answer == -1:
            return nums[0]
        else:
            return answer

    def peak_element(self, arr):

        start = 0
        end = len(arr) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if end > mid and arr[mid] > arr[mid + 1]:
                return arr[mid + 1]
            elif mid > start and arr[mid] < arr[mid - 1]:
                return arr[mid]
            elif arr[start] > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    # Time Complexity: O(log(n)), Space Complexity: O(1)
