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

    # Second Solution: same time and space complexity

    # class Solution(object):
    #     def maxValue(self, n, index, maxSum):
    #         """
    #         :type n: int
    #         :type index: int
    #         :type maxSum: int
    #         :rtype: int
    #         """
    #
    #         start = 1
    #         end = maxSum
    #         answer = 0
    #         while start <= end:
    #
    #             mid = start + (end - start) // 2
    #
    #             Element_on_left = index
    #             if Element_on_left < 0:
    #                 Element_on_left = 0
    #             Element_on_right = (n - 1) - index
    #
    #             left_sum = self.sum_on_two_sides(Element_on_left, mid - 1)
    #             right_sum = self.sum_on_two_sides(Element_on_right, mid - 1)
    #
    #             if mid + left_sum + right_sum <= maxSum:
    #                 answer = max(answer, mid)
    #                 start = mid + 1
    #             else:
    #                 end = mid - 1
    #
    #         return answer
    #
    #     def sum_on_two_sides(self, element, val):
    #         val_sum_of_element = val * (val + 1) / 2
    #         remaining_sum = val - element
    #         if remaining_sum < 0:
    #             return val_sum_of_element + abs(remaining_sum)
    #         else:
    #             out_of_bound_sum = remaining_sum * (remaining_sum + 1) / 2
    #             return val_sum_of_element - out_of_bound_sum

