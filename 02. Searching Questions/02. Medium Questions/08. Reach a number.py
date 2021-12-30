class Solution:

    # https://leetcode.com/problems/reach-a-number/

    def reachNumber(self, target: int) -> int:

        target = abs(target)
        total = 0
        step = 1

        while True:
            total += step

            if total >= target and total % 2 == target % 2:
                return step

            step += 1

        # Space Complexity: O(1), Time Complexity: O(2^N)
