class Solution:

    # https://leetcode.com/problems/two-sum/

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashtable = {}

        for index, value in enumerate(nums):

            m = target - value

            if m in hashtable:
                return [hashtable[m], index]
            else:
                hashtable[value] = index

    # Time Complexity: O(n), Space Complexity: O(m) m: hashtable
