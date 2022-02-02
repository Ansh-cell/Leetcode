class Solution:

    # https://leetcode.com/problems/squares-of-a-sorted-array/

    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        nums.sort()
        return nums

    # Time Complexity: O(n*log(n)), Space Complexity: O(1) : if we are allowed to make changes in original array
    # otherwise O(len(nums))

    # class Solution:
    #     def sortedSquares(self, nums: List[int]) -> List[int]:
    #         answer = [None] * len(nums)
    #         left, right = 0, len(nums) - 1
    #
    #         for i in range(len(nums) - 1, -1, -1):
    #
    #             if abs(nums[left]) > abs(nums[right]):
    #                 answer[i] = nums[left] ** 2
    #                 left += 1
    #             else:
    #                 answer[i] = nums[right] ** 2
    #                 right -= 1
    #
    #         return answer

    # Time Complexity: O(n), Space Complexity: O(len(nums))

