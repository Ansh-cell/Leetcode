class Solution:

    # https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

    def average(self, salary: List[int]) -> float:
        salary.sort()
        total_answer = 0

        for i in range(1, len(salary) - 1):
            total_answer += salary[i]

        return total_answer / (len(salary) - 2)

    # Time Complexity: O(n*log(n)), Space Complexity: O(1)
