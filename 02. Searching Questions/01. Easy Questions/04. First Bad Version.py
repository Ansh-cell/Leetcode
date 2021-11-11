# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


# https://leetcode.com/problems/first-bad-version/submissions/


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 1
        end = n
        potential_answer = 0
        if n == 1:
            return 1

        while start < end:

            mid = start + (end - start) // 2
            is_faulty = isBadVersion(mid)

            if is_faulty:
                potential_answer = mid
                end = mid - 1
            else:
                start = mid + 1

        if isBadVersion(start):
            return start
        else:
            return potential_answer