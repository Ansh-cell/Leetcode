class Solution:

    #https://leetcode.com/problems/minimum-absolute-difference/

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        answer = []
        arr.sort()

        left_pointer = 0
        right_pointer = 1

        curr_minimum = float('inf')

        while left_pointer <= len(arr) - 2 and right_pointer <= len(arr) - 1:

            if arr[right_pointer] - arr[left_pointer] < curr_minimum:
                answer = [[arr[left_pointer], arr[right_pointer]]]
                curr_minimum = arr[right_pointer] - arr[left_pointer]
            elif arr[right_pointer] - arr[left_pointer] == curr_minimum:
                answer.append([arr[left_pointer], arr[right_pointer]])
            left_pointer += 1
            right_pointer += 1

        return answer

    # Time Complexity: O(n * log(n)), Space Complexity: O(n)
