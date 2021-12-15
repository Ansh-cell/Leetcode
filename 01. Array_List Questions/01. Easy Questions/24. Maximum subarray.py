class Solution:

    # https://leetcode.com/problems/maximum-subarray/

    def maxSubArray(self, nums: List[int]) -> int:

        answer = nums[0]
        sub_array_sum = 0

        for i in nums:

            if sub_array_sum < 0:
                sub_array_sum = 0
            sub_array_sum += i
            answer = max(sub_array_sum, answer)
        return answer

    #   Time Complexity: O(n) and Space Complexity: O(1)
