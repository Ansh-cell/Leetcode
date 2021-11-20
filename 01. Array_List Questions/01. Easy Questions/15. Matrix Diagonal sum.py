class Solution:

    # https://leetcode.com/problems/matrix-diagonal-sum/

    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        col_start = 0
        col_end = len(mat) - 1
        for i in range(len(mat)):
            if col_end == col_start:
                summ += mat[i][col_start]
            else:
                summ += mat[i][col_start]
                summ += mat[i][col_end]
            col_start += 1
            col_end -= 1

        return summ

    # Time Complexity: O(n) n: row of a matrix, Space Complexity: O(1)
