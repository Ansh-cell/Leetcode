class Solution:

    #  https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

    def sumZero(self, n: int) -> List[int]:

        return self.random_list(n)

    def random_list(self, number):
        answer = []
        ignore_zero = False
        loop_number = 0
        if number % 2 == 0:
            ignore_zero = True
            loop_number = int(number / 2)
        else:
            loop_number = int(number / 2)

        for x in range(-loop_number, loop_number + 1):

            if x == 0:
                if ignore_zero:
                    pass
                else:
                    answer.append(x)
            else:
                answer.append(x)

        return answer

    # Time Complexity: O(N), Space Complexity: O(N)
