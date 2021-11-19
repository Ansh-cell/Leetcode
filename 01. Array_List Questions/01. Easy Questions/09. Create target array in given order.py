class Solution:

    # https://leetcode.com/problems/create-target-array-in-the-given-order/

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i in range(len(nums)):
            insert_index = index[i]
            target.insert(insert_index, nums[i])

        return target
    # Time Complexity: O(n), Space Complexity: O(n)
