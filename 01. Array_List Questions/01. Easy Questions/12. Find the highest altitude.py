class Solution:

    # https://leetcode.com/problems/find-the-highest-altitude/

    def largestAltitude(self, gain: List[int]) -> int:

        high_altitude = 0
        x = 0
        for i in gain:
            x = x + i
            if x > high_altitude:
                high_altitude = x

        return high_altitude

    # Time Complexity: O(n), Space Complexity: O(1)
