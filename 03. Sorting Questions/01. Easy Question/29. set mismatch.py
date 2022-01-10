class Solution:

    # https://leetcode.com/problems/set-mismatch/

    def findErrorNums(self, nums: List[int]) -> List[int]:
        answer = []
        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        for i in range(len(nums)):

            if i + 1 != nums[i]:
                answer.append(nums[i])
                answer.append(i + 1)

        return answer

    # Time Complexity: O(n), Space Complexity: O(1)
