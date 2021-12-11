class Solution:

    # https://leetcode.com/problems/maximum-population-year/

    def maximumPopulation(self, logs: List[List[int]]) -> int:
        imaginary_array = [0] * 101

        for start, end in logs:
            imaginary_array[start - 1950] += 1
            imaginary_array[end - 1950] -= 1

        max_population = 0
        year = 1950
        running_sum = 0

        for index, value in enumerate(imaginary_array):
            running_sum += value

            if running_sum > max_population:
                max_population = running_sum
                year = 1950 + index
        return year

    # Time Complexity: O(n) n: length of imaginary_array, Space Complexity: O(n)
