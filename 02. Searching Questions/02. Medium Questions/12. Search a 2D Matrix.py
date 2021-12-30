class Solution:

    # https://leetcode.com/problems/search-a-2d-matrix/

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        index = self.binary_search_row(target, 0, matrix)
        answer = self.binary_search_column(target, index, matrix)
        return answer

    def binary_search_row(self, target, column, matrix):

        start = 0
        end = len(matrix) - 1
        answer = 0
        while start <= end:

            mid = start + (end - start) // 2

            if matrix[mid][column] == target:
                return mid
            elif matrix[mid][column] > target:
                end = mid - 1
            else:
                answer = mid
                start = mid + 1

        return answer

    def binary_search_column(self, target, row, matrix):

        start = 0
        end = len(matrix[0]) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False

    # Time Complexity: O(logn), Space Complexity: O(1)
