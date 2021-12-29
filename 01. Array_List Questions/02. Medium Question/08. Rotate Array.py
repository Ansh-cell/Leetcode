class Solution:

    # https://leetcode.com/problems/rotate-array/

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k is None or k <= 0:
            return
        else:
            end = len(nums) - 1
            k = k % len(nums)
            self.reverse(nums, 0, end - k)
            self.reverse(nums, end - k + 1, end)
            self.reverse(nums, 0, end)

    def reverse(self, array, start, end):
        while start < end:
            array[end], array[start] = array[start], array[end]
            start, end = start + 1, end - 1

    # Time Complexity: O(n), Space Complexity: O(1)
