class Solution:

    # https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        for _ in range(4):
            if self.check(mat, target) is True:
                return True
            else:
                mat = self.transpose(mat)
                mat = self.swap(mat)
        return False

    def transpose(self, mat):
        return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]  # O(n^2)

    def swap(self, matrix):  # O(n^2)
        loop = 0
        if len(matrix) % 2 == 0:
            loop = int(len(matrix) / 2)
        else:
            loop = int(len(matrix) / 2)

        for i in range(len(matrix)):
            x = -1
            for j in range(loop):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][x]
                matrix[i][x] = temp
                x -= 1
        return matrix

    def check(self, rotated_mat, target):  # O(n^2)

        for i in range(len(rotated_mat)):
            for j in range(len(rotated_mat[i])):
                if rotated_mat[i][j] != target[i][j]:
                    return False
        return True

    # Time Complexity: O(n^2), Space Complexity: O(n)

#   Second Solution

# class Solution:
#     def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
#
#         for _ in range(4):
#             if mat == target:
#                 return True
#             else:
#                 mat = [list(x) for x in zip(*mat[::-1])]
#         return False

# Time Complexity: O(n), Space Complexity: O(n)
