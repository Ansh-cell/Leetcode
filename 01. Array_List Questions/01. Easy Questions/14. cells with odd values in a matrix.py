# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:

        matrix = self.apply_increment(m, n, indices)
        return self.check_odd(matrix)

    def apply_increment(self, m, n, indices):

        zero_matrix = []    # Space Complexity: O(m + n)

        for i in range(m):      # Time Complexity: O(m*n)
            a = []
            for j in range(n):
                a.append(0)
            zero_matrix.append(a)

        for r, c in indices:        # Time Complexity: O(m^2 + m*n)

            for i in range(len(zero_matrix[r])):    # Time Complexity: O(n) n: column
                zero_matrix[r][i] += 1
            for j in range(len(zero_matrix)):   # Time Complexity: O(m) m: row
                zero_matrix[j][c] += 1

        return zero_matrix

    def check_odd(self, matrix):        # Time Complexity: O(m*n)
        count = 0
        for i in range(len(matrix)):

            for j in range(len(matrix[i])):

                if matrix[i][j] % 2 != 0:
                    count += 1

        return count

    # Time Complexity: O(m^2 + m*n), Space Complexity: Space Complexity: O(m + n)
