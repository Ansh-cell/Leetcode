class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []
        nums.sort()

        for index, value in enumerate(nums):

            if index > 0 and value == nums[index - 1]:
                continue

            left_pointer = index + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                threeSum = value + nums[left_pointer] + nums[right_pointer]

                if threeSum > 0:
                    right_pointer -= 1
                elif threeSum < 0:
                    left_pointer += 1
                else:
                    answer.append([value, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1

                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1

        return answer

    # Time Complexity: O(N^2), Space Complexity: O(1)
