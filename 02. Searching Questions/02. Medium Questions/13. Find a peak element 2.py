class Solution:

    # https://leetcode.com/problems/find-a-peak-element-ii/

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        start_row = 0
        end_row = len(mat) - 1

        while start_row <= end_row:
            max_col = 0
            mid_row = start_row + (end_row - start_row) // 2

            for col in range(len(mat[0])):
                if mat[mid_row][col] >= mat[mid_row][max_col]:
                    max_col = col

            up_is_big = mid_row - 1 >= start_row and mat[mid_row - 1][max_col] > mat[mid_row][max_col]
            down_is_big = mid_row + 1 <= end_row and mat[mid_row + 1][max_col] > mat[mid_row][max_col]

            if (not up_is_big) and (not down_is_big):
                return mid_row, max_col
            elif up_is_big:
                end_row = mid_row - 1
            else:
                start_row = mid_row + 1
        return []

    # Time Complexity: O(n * log(m)), Space Complexity: O(1)
