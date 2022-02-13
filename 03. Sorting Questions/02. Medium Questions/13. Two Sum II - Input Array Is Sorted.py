class Solution:

    # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:

            summation = numbers[left_pointer] + numbers[right_pointer]

            if summation == target:
                return [left_pointer + 1, right_pointer + 1]
            elif summation > target:
                right_pointer -= 1
            else:
                left_pointer += 1

    # Time Complexity: O(n), Space Complexity: O(1)
