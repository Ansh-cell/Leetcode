class Solution:

    # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0
        end = len(numbers) - 1

        while start < end:  # Time Complexity: O(n) --> Linear Time --> decent solution tbh

            sum_of_2_numbers = numbers[start] + numbers[end]

            if sum_of_2_numbers == target:
                return start + 1, end + 1
            elif sum_of_2_numbers > target:
                end = end - 1
            else:
                start = start + 1

        # space complexity: O(1) --> Linear --> Very good
