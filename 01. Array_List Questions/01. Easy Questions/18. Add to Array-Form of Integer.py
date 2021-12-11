class Solution:

    # https://leetcode.com/problems/add-to-array-form-of-integer/

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        loop_timer = True
        array_index = len(num) - 1
        while loop_timer:
            if array_index > -1:
                num[array_index] = num[array_index] + k
                if len(str(num[array_index])) > 1:
                    loop_timer = True
                else:
                    loop_timer = False
                Quotient, remainder = divmod(num[array_index], 10)
                num[array_index] = remainder
                k = Quotient
                array_index -= 1
            else:
                if len(str(k)) > 1:
                    loop_timer = True
                else:
                    loop_timer = False
                Quotient, remainder = divmod(k, 10)
                num.insert(0, remainder)
                k = Quotient
        return num

        # Time Complexity: O(n), Space Complexity: O(1)
