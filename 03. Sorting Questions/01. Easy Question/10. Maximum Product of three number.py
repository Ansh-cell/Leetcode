class Solution:

    # https://leetcode.com/problems/maximum-product-of-three-numbers/

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

    # Time Complexity: O(n*log(n)), Space Complexity: O(1) : if we dont need original array otherwise O(len(nums))
