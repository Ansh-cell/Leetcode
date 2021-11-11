# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


# https://leetcode.com/problems/guess-number-higher-or-lower/submissions/

class Solution:
    def guessNumber(self, n: int) -> int:

        start = 1
        end = n

        while start <= end:

            mid = start + (end - start) // 2

            is_my_guess_correct = guess(mid)

            if is_my_guess_correct == 0:
                return mid
            elif is_my_guess_correct == 1:
                start = mid + 1
            else:
                end = mid - 1