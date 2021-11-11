import math


class Solution:
    def mySqrt(self, x: int) -> int:

        start = 0
        end = x

        while start < end:

            mid = math.ceil((start + end) / 2)

            if mid * mid <= x:
                start = mid
            else:
                end = mid - 1

        return int(start)
