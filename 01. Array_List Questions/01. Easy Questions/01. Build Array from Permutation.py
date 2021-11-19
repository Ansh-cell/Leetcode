class Solution(object):

    # https://leetcode.com/problems/build-array-from-permutation/

    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []

        for i in range(len(nums)):
            arr.append(nums[nums[i]])

        return arr
    # Time Complexity: O(n), Space Complexity: O(n)
