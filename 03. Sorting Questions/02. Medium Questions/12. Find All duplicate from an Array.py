class Solution:

    # https://leetcode.com/problems/find-all-duplicates-in-an-array/

    def findDuplicates(self, nums: List[int]) -> List[int]:

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

        return answer

    # Time Complexity: O(n), Space Complexity: O(1) : if we don't include our answer otherwise O(n)
