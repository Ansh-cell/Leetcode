class Solution:

    # https://leetcode.com/problems/max-value-of-equation/

    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        answer = float('-inf')
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                abs_qu = abs(points[i][0] - points[j][0])
                equ = abs_qu + points[i][1] + points[j][1]
                if abs_qu <= k and equ > answer:
                    answer = equ

        return answer

    # Time Complexity: O(n^2), Space Complexity: O(1)

    # Time complexity can be optimised with queue, but I haven't learned that yet so I will optimise this
    # solution in Queue section
