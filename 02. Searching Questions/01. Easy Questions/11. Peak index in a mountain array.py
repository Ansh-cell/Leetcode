class Solution:

    # https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/

    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        start = 0
        end = len(arr) - 1

        while start < end:

            mid = start + (end - start) // 2

            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid

        return start

    # Time Complexity: O(log(n)), Space Complexity: O(1)
