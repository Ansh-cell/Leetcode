class Solution(object):

    # https://leetcode.com/problems/set-matrix-zeroes/

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        zeroth_row = False

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    if r == 0:
                        zeroth_row = True
                        matrix[0][c] = 0
                    else:
                        # set imaginary row to 0
                        matrix[r][0] = 0
                        # set imaginary column to 0
                        matrix[0][c] = 0

        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for i in range(len(matrix[row])):
                    matrix[row][i] = 0

        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                for i in range(len(matrix)):
                    matrix[i][col] = 0

        if zeroth_row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        # Time Complexity: O(M*N), Space Complexity: O(1)
