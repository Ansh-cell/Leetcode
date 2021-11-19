class Solution(object):

    # https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        arr = [False] * len(candies)
        max_element = max(candies)

        for i in range(len(candies)):
            candy_incl = candies[i] + extraCandies

            if candy_incl >= max_element:
                arr[i] = True
            else:
                arr[i] = False

        return arr

    # Time Complexity: O(n), Space Complexity: O(1)
