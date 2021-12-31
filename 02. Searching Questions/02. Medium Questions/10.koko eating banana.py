import math


class Solution:

    # https://leetcode.com/problems/koko-eating-bananas/

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        answer = float('inf')
        while start <= end:

            mid = start + (end - start) // 2
            ans = self.computation(piles, mid)

            if ans <= h:
                answer = min(answer, mid)
                end = mid - 1
            else:
                start = mid + 1

        return answer

    def computation(self, piles, mid):
        total_hour = 0
        for i in range(len(piles)):
            total_hour += math.ceil(piles[i] / mid)
        return total_hour

    # Time Complexity: O(log(max(p))*p), Space Complexity: O(1)
