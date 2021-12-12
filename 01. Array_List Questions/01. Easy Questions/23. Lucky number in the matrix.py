class Solution:

    # https://leetcode.com/problems/lucky-numbers-in-a-matrix/

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        for i in range(len(matrix)):
            min_num = min(min(list(zip(matrix))[i]))
            min_num_index = matrix[i].index(min_num)
            is_max = True
            for j in range(len(matrix)):
                if matrix[j][min_num_index] > min_num:
                    is_max = False
                    break
            if is_max:
                return [min_num]

    # Time Complexity: O(n * m) n: lenght of row, m: length of column, Space Complexity: O(1)
