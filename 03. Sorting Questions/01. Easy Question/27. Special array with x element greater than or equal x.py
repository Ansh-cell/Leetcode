class Solution:

    # https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

    def specialArray(self, nums: List[int]) -> int:

        answer = len(nums)
        nums.sort()

        while answer >= 0:
            count = 0
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] >= answer:
                    count += 1
                else:
                    break
            if count == answer:
                return answer
            else:
                answer -= 1
        return -1

    # Time Complexity: O(M*N), Space Complexity: O(n)

    # not a best solution better to use binary search
