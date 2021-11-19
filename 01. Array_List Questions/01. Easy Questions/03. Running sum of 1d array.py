class Solution(object):

    # https://leetcode.com/problems/running-sum-of-1d-array/

    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [0] * len(nums)
        arr[0] = nums[0]

        for i in range(1, len(nums)):
            sum_till_now = arr[i - 1]
            arr[i] = (sum_till_now + nums[i])

        return arr

    # Time Complexity: O(n), Space Complexity: O(1)
