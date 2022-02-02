class Solution:

    # https://leetcode.com/problems/height-checker/submissions/

    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        count = 0
        for i in range(len(heights)):

            if heights[i] != expected[i]:
                count += 1

        return count

    # Time Complexity: O(n*log(n)), Space Complexity: O(n)
