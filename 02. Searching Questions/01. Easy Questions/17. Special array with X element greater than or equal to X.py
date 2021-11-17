class Solution:

    # https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

    """def specialArray(self, nums: List[int]) -> int:

        for special_num in range(len(nums) + 1):
            count = 0
            for num in nums:
                if num >= special_num:
                    count += 1

            if count == special_num:
                return special_num

        return -1"""

    #  Time Complexity: O(n^2), Space Complexity: O(1)


