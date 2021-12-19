class Solution:

    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    def removeDuplicates(self, nums: List[int]) -> int:

        check = float('-inf')
        count = 0
        index = 0

        for i in range(len(nums)):

            if nums[i] > check:
                check = nums[i]
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
                count += 1

        return count

    # Time Complexity: O(n), Space Complexity: O(1)
