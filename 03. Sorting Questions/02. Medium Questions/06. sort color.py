# class Solution:
#
#     # https://leetcode.com/problems/sort-colors/
#
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         color_0 = 0
#         color_1 = 0
#         color_2 = 0
#
#         for i in nums:
#             if i == 0:
#                 color_0 += 1
#             elif i == 1:
#                 color_1 += 1
#             else:
#                 color_2 += 1
#
#         for i in range(len(nums)):
#
#             if color_0 != 0:
#                 nums[i] = 0
#                 color_0 -= 1
#             elif color_1 != 0:
#                 nums[i] = 1
#                 color_1 -= 1
#             else:
#                 nums[i] = 2
#                 color_2 -= 1
#
#     # Time Complexity: O(n), Space Complexity: O(1)
#     # it is a good solution but we are not sorting the the array with single pass

class Solution:

    # https://leetcode.com/problems/sort-colors/

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        index = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while index <= r:

            if nums[index] == 0:
                swap(l, index)
                l += 1

            if nums[index] == 2:
                swap(r, index)
                r -= 1
                index -= 1

            index += 1

    # Time Complexity: O(n), Space Complexity: O(1)
    # we are sorting in single pass
