class Solution:

    # https://leetcode.com/problems/matrix-cells-in-distance-order/

    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        def distance(answer):
            p1, p2 = answer
            return abs(rCenter - p1) + abs(cCenter - p2)

        answer = []

        for i in range(rows):
            for j in range(cols):
                answer.append([i, j])

        return sorted(answer, key=distance)

    # Time Complexity: O(rows*cols) --> O(n^2), Space Complexity: O(n)
