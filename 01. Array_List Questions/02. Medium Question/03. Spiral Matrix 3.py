class Solution:

    # https://leetcode.com/problems/spiral-matrix-iii/

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        return self.spiral_matrix_3(rows, cols, rStart, cStart)

    def spiral_matrix_3(self, row, column, rstart, cstart):
        answer = []
        count = 0
        matrix_range = row * column
        left, right = cstart, cstart + 2
        top, bottom = rstart, rstart + 2

        while count < matrix_range:
            t_left, t_right = left, right
            t_top, t_down = top, bottom

            # first top row
            for i in range(left, right):
                if self.check_grid(top, i, row, column):
                    answer.append([top, i])
                    count += 1
            top += 1

            # right side column
            for i in range(top, bottom):
                if self.check_grid(i, right - 1, row, column):
                    answer.append([i, right - 1])
                    count += 1
            right -= 1

            for i in range(right - 1, left - 1, -1):
                if self.check_grid(bottom - 1, i, row, column):
                    answer.append([bottom - 1, i])
                    count += 1
            bottom -= 1

            for i in range(bottom, top - 2, -1):
                if self.check_grid(i, left - 1, row, column):
                    answer.append([i, left - 1])
                    count += 1

            left, right = t_left - 1, t_right + 1
            top, bottom = t_top - 1, t_down + 1

        return answer

    def check_grid(self, r, c, row, column):
        if r >= 0 and c >= 0:
            if r <= row - 1 and c <= column - 1:
                return True
            else:
                return False
        else:
            return False


    # Time Complexity: O(m*n), Space Complexity: O(m*n) if we include our answer otherwise O(1)
