class Solution:

    # https://leetcode.com/problems/sort-colors/

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        comman_index = 0

        # sort 0
        for i in range(comman_index, len(nums)):
            if nums[i] == 0:
                nums[comman_index], nums[i] = nums[i], nums[comman_index]
                comman_index += 1

        # sort 1
        for i in range(comman_index, len(nums)):
            if nums[i] == 1:
                nums[comman_index], nums[i] = nums[i], nums[comman_index]
                comman_index += 1

        # sort 2
        for i in range(comman_index, len(nums)):
            if nums[i] == 2:
                nums[comman_index], nums[i] = nums[i], nums[comman_index]
                comman_index += 1

        # Time Complexity: O(n), Space Complexity: O(1)
