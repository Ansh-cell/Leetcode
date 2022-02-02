class Solution:

    # https://leetcode.com/problems/largest-perimeter-triangle/

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        first_index = -1
        second_index = -2
        third_index = -3

        for i in range(len(nums)):

            if first_index >= -len(nums) and second_index >= -len(nums) and third_index >= -len(nums) and \
                    nums[first_index] + nums[second_index] > nums[third_index]:
                if first_index >= -len(nums) and second_index >= -len(nums) and third_index >= -len(nums) and \
                        nums[third_index] + nums[second_index] > nums[first_index]:
                    if first_index >= -len(nums) and second_index >= -len(nums) and third_index >= -len(nums) and \
                            nums[first_index] + nums[third_index] > nums[second_index]:
                        return nums[first_index] + nums[second_index] + nums[third_index]
                    else:
                        first_index -= 1
                        second_index -= 1
                        third_index -= 1
                else:
                    first_index -= 1
                    second_index -= 1
                    third_index -= 1
            else:
                first_index -= 1
                second_index -= 1
                third_index -= 1
        return 0
