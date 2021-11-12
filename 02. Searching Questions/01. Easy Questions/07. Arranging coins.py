class Solution:

    # https://leetcode.com/problems/arranging-coins/submissions/

    def arrangeCoins(self, n: int) -> int:

        start = 1
        end = n
        if n == 1 or n == 2:
            return 1
        while start <= end:

            mid = start + (end - start) // 2
            # now we can check at mid how many coins are used
            coin_used = (mid + 1) * (mid) / 2

            if coin_used == n:
                return mid
            elif coin_used < n:
                start = mid + 1
            else:
                end = mid - 1

        return end

        # Time complexity: O(log(n)), Space Complexity: O(1)


