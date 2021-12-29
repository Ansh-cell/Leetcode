class Solution:

    # https://leetcode.com/problems/jump-game/

    def canJump(self, nums: List[int]) -> bool:

        goal_post = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal_post:
                goal_post = i

        if goal_post == 0:
            return True
        else:
            return False

        # Time Complexity: O(n), Space Complexity: O(1)
