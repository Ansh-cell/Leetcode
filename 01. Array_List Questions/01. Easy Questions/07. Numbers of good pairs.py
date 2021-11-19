class Solution(object):

    # https://leetcode.com/problems/number-of-good-pairs/

    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1

        return count

    # Time Complexity: O(n^2), Space Complexity: O(1)
