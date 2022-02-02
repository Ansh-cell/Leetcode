class Solution:

    # https://leetcode.com/problems/sort-array-by-parity-ii/

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums.sort()
        even_index = 0

        for i in range(len(nums)):

            if nums[i] % 2 == 0:
                nums[i], nums[even_index] = nums[even_index], nums[i]
                even_index += 1

        odd_index_from_back = -2
        for j in range(1, int(len(nums) / 2), 2):
            nums[j], nums[odd_index_from_back] = nums[odd_index_from_back], nums[j]
            odd_index_from_back -= 2

        return nums

    # Time Complexity: O(n*log(n)), Space Complexity: O(1)
