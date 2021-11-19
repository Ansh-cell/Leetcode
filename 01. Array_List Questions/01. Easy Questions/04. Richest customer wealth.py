class Solution(object):

    # https://leetcode.com/problems/richest-customer-wealth/

    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        max_sum = 0

        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]

            if wealth > max_sum:
                max_sum = wealth

        return max_sum

    # Time Complexity: O(n*m) where n --> number of rows, m --> number of column, Space Complexity: O(1)
