# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#
#         new_matrix = [[None] * c for _ in range(r)]
#
#         new_mat_col = 0
#         new_mat_row = 0
#
#         total_number_of_block_left = r * c
#
#         for i in range(len(mat)):
#             for j in range(len(mat[i])):
#                 if total_number_of_block_left != 0:
#                     if new_mat_col < c:
#                         new_matrix[new_mat_row][new_mat_col] = mat[i][j]
#                         total_number_of_block_left -= 1
#                         new_mat_col += 1
#                     else:
#                         new_mat_row += 1
#                         new_mat_col = 0
#                         new_matrix[new_mat_row][new_mat_col] = mat[i][j]
#                         total_number_of_block_left -= 1
#                         new_mat_col += 1
#                 else:
#                     return mat
#             if new_mat_col == c:
#                 new_mat_row += 1
#                 new_mat_col = 0
#         if total_number_of_block_left == 0:
#             return new_matrix
#         else:
#             return mat

# Time Complexity: O(n*m), Space Complexity: O(n*m)

# def matrixReshape(mat, r, c):
#     if len(mat) == 0 or r * c != len(mat) * len(mat[0]):
#         return mat
#     row, col = 0, 0
#
#     new_matrix = [[None for _ in range(c)] for _ in range(r)]
#
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             new_matrix[row][col] = mat[i][j]
#             col += 1
#             if col == c:
#                 row += 1
#                 c = 0
#     return new_matrix
