class Solution:

    # https://leetcode.com/problems/find-the-duplicate-number/

    def findDuplicate(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            cur = abs(num)

            if nums[cur] < 0:
                answer = cur
                break
            nums[cur] = -nums[cur]

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return answer

    # Time Complexity: O(n), Space Complexity: O(1)
