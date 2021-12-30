class Solution:

    # https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

    def maxValue(self, n: int, i: int, maxSum: int) -> int:
        start, end = 1, maxSum  # maxValue possible at index is in range [1, maxSum]
        res = 0
        while (start <= end):
            mid = start + (end - start) // 2

            eleOnLeft = min(i, mid - 1)
            leftSum = self.sum(eleOnLeft, mid - 1)
            leftSum += max(0, i - mid + 1)  # Adding the remaining 1's to the leftSum

            eleOnRight = min(n - i - 1, mid - 1)
            rightSum = self.sum(eleOnRight, mid - 1)
            rightSum += max(0, n - i - 1 - mid + 1)  # Adding the remaining 1's to the RightSum

            if mid + leftSum + rightSum <= maxSum:
                res = max(res, mid)
                start = mid + 1
            else:
                end = mid - 1

        return res

    def sum(self, ele, x):

        totalSum = x * (x + 1) // 2
        rem = x - ele
        partialSum = rem * (rem + 1) // 2
        return totalSum - partialSum

    # Time Complexity: O(logn), Space Complexity: O(1)
