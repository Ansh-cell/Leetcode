class Solution:

    # https://leetcode.com/problems/majority-element/

    def majorityElement(self, nums: List[int]) -> int:

        res, count = 0, 0

        for i in nums:
            if count == 0:
                res = i
            count += (1 if i == res else -1)
        return res

    # Time Complexity: O(n), Space Complexity: O(1)
