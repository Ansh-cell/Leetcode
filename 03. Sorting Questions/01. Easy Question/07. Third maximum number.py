class Solution:

    # https://leetcode.com/problems/third-maximum-number/

    def thirdMax(self, nums: List[int]) -> int:

        nums = set(nums)
        nums = sorted(list(nums))

        if len(nums) > 2:
            nums.pop()
            nums.pop()
            return nums[-1]
        else:
            return nums[-1]

        # Time Complexity: O(n*log(n)), Space Complexity: O(n)
