import math


class Solution:

    # https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0

        for i in nums:
            if int(math.log10(i) + 1) % 2 == 0:
                even_count += 1
        return even_count

    # Time Complexity: O(n), Space Complexity: O(1)
