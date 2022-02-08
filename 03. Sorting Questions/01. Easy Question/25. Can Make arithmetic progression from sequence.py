class Solution:

    # https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        left_pointer = 0
        right_pointer = 1
        answer = abs(arr[left_pointer] - arr[right_pointer])

        while left_pointer <= len(arr) - 2 and right_pointer <= len(arr) - 1:

            if abs(arr[left_pointer] - arr[right_pointer]) != answer:
                return False
            left_pointer += 1
            right_pointer += 1

        return True

    # Time Complexity: O(n*log(n)), Space Complexity: O(1)
