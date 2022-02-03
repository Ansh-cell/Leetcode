from operator import itemgetter


class Solution:

    # https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

    def sortByBits(self, arr: List[int]) -> List[int]:

        if len(arr) == 0:
            return []
        elif len(arr) == 1:
            return arr
        else:
            for i in range(len(arr)):
                bits = bin(arr[i]).count("1")
                arr[i] = [arr[i], bits]
            arr = sorted(arr, key=itemgetter(1, 0))
            for i in range(len(arr)):
                arr[i] = arr[i][0]
            return arr

    # Time Complexity: O(n*log(n)), Space Complexity: O(1)
