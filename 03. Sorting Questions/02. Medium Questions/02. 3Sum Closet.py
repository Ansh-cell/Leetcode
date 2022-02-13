class Solution:

    # https://leetcode.com/problems/3sum-closest/

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        difference = float('inf')
        answer = 0

        for i in range(len(nums)):

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum == target:
                    return target
                elif abs(nums[i] + nums[l] + nums[r] - target) < difference:
                    difference = abs(nums[i] + nums[l] + nums[r] - target)
                    answer = threeSum
                if threeSum > target:
                    r -= 1
                else:
                    l += 1

        return answer

    # Time Complexity: O(n^2), Space Complexity: O(1)
