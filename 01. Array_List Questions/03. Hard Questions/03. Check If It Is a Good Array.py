import math
class Solution:

    # https://leetcode.com/problems/check-if-it-is-a-good-array/

    def isGoodArray(self, nums: List[int]) -> bool:
        import math
        n = len(nums)
        if n ==1:
            return nums[0] ==1
        d = math.gcd(nums[0], nums[1])
        if d == 1:
            return True
        else:
            for i in range(2, n):
                d = math.gcd(nums[i], d)
                if d == 1:
                    return True
            return False

        # Time Complexity: O(n), Space Complexity: O(1)
