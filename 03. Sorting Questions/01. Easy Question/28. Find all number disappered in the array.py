class Solution:

    # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        answer = []
        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                answer.append(i + 1)
        return answer

    # Time Complexity: O(n), Space Complexity: O(1) if we don't include answer array
