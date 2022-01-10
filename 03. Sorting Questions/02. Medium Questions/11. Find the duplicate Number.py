class Solution:

    # https://leetcode.com/problems/find-the-duplicate-number/

    def findDuplicate(self, array: List[int]) -> int:

        i = 0
        while i < len(array):
            correct_index = array[i] - 1
            if array[i] == array[correct_index] and i != correct_index:
                return array[i]
            elif array[i] != array[correct_index]:
                array[correct_index], array[i] = array[i], array[correct_index]
            else:
                i += 1

    # Time Complexity: O(n), Space Complexity: O(1)
