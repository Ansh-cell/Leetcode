class Solution:

    # https://leetcode.com/problems/spiral-matrix-ii/

    def generateMatrix(self, n: int) -> List[List[int]]:
        x = [([0] * n) for i in range(n)]
        count = 1
        left, right = 0, n
        top, down = 0, n
        while count <= n*n:

            for i in range(left, right):
                x[top][i] = count
                count += 1
            top += 1

            for i in range(top, down):
                x[i][right - 1] = count
                count += 1
            right -= 1

            for i in range(right - 1, left - 1, -1):
                x[down - 1][i] = count
                count += 1
            down -= 1

            for i in range(down - 1, top - 1, -1):
                x[i][left] = count
                count += 1
            left += 1

        return x

    # Time Complexity: O(n*n), Space Complexity: O(n*n)
