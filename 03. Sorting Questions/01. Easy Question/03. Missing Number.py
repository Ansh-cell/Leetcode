class Solution:

    # https://leetcode.com/problems/missing-number/

    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct_index = nums[i]
            if nums[i] < len(nums) and nums[i] != nums[correct_index]:
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return nums[-1] + 1

    # Time Complexity: O(n), Space Complexity: O(1)
