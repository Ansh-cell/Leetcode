class Solution:

    # https://leetcode.com/problems/house-robber/

    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    # Time Complexity: O(n), Space Complexity: O(1)
