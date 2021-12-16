class Solution:

    # https://leetcode.com/problems/plus-one/

    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        for i in range(len(digits) - 1, -1, -1):
            new_answer = digits[i] + num
            remainder = new_answer % 10
            Quotient = new_answer // 10

            digits[i] = remainder
            num = Quotient

        if num:
            digits.insert(0, num)
        return digits

    # Time Complexity: O(n), Space Complexity: O(1)
