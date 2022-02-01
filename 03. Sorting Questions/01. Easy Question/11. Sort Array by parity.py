class Solution:

    # https://leetcode.com/problems/sort-array-by-parity/

    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        even_index = 0

        for i in range(len(nums)):

            if nums[i] % 2 == 0:
                nums[even_index], nums[i] = nums[i], nums[even_index]
                even_index += 1

        return nums

    # Time Complexity: O(n), Space Complexity: O(1)
