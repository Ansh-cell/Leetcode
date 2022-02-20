class Solution:

    # https://leetcode.com/problems/kth-largest-element-in-an-array/

    def findKthLargest(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums) < k:
            return nums[0]
        else:
            nums.sort()
            x = -k
            return nums[x]

    # Time Complexity: O(n*log(n)), Space Complexity: O(1) : if we dont care about original array

    # otherwise, Space Complexity: O(n)

