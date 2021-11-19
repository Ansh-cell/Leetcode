class Solution(object):

    # https://leetcode.com/problems/concatenation-of-array/

    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        arr = [0] * (2 * len(nums))

        for i in range(len(nums)):
            arr[i] = nums[i]
            arr[i + len(nums)] = nums[i]

        return arr
    # Time Complexity: O(n), Space Complexity: O(n)
