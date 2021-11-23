class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        result_matrix = []
        for i in range(len(matrix[0])):
            x = []
            for j in range(len(matrix)):
                item = matrix[j][i]
                x.append(item)
            result_matrix.append(x)
        return result_matrix

    # Time Complexity: O(r * c), Space Complexity: O(r * c)
