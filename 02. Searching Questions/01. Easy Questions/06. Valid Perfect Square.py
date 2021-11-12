class Solution:

    # https://leetcode.com/problems/valid-perfect-square/submissions/

    def isPerfectSquare(self, num: int) -> bool:

        start = 0
        end = num

        while start <= end:  # Time Complexity: O(log(n)) --> Nice solution

            mid = start + (end - start) // 2
            check = mid * mid

            if check == num:
                return True
            elif check > num:
                end = mid - 1
            else:
                start = mid + 1

        return False

        # Space Complexity: O(1) --> Linear --> Excellent
