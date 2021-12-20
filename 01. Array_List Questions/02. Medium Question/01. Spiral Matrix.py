class Solution:

    # https://leetcode.com/problems/spiral-matrix/

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, down = 0, len(matrix)
        result = []

        if len(matrix) == 1:
            return matrix[0]
        elif len(matrix) == 2:
            matrix[1].reverse()
            return matrix[0] + matrix[1]
        else:
            while left < right and top < down:

                # inserted left to right into result
                for i in range(left, right):
                    result.append(matrix[top][i])
                top += 1

                # inserted right column into result
                for i in range(top, down):
                    result.append(matrix[i][right - 1])
                right -= 1

                if not (left < right and top < down):
                    break
                # inserted bottom row into result
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[down - 1][i])
                down -= 1

                for i in range(down - 1, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

            return result

        # Time Complexity: 0(m*n), Space Complexity: O(1): if we ignore output list otherwise O(m*n)
