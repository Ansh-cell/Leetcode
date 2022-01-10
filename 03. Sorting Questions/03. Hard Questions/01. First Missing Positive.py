class Solution:

    # https://leetcode.com/problems/first-missing-positive/

    def firstMissingPositive(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1

            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[correct_index]:
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
            else:
                i += 1

        for i in range(len(nums)):

            if i + 1 != nums[i]:
                return i + 1
        return nums[-1] + 1

    # Time Complexity: O(n), Space Complexity: O(1)
