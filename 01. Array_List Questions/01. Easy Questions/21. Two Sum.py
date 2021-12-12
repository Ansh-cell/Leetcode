class Solution:

    # https://leetcode.com/problems/two-sum/

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for index, value in enumerate(nums):

            m = target - value
            if m in d:
                return [index, d[m]]
            else:
                d[value] = index

                # Time Complexity: O(N), Space Complexity: O(N)
