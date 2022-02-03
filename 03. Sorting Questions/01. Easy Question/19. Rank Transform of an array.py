class Solution:

    # https://leetcode.com/problems/rank-transform-of-an-array/

    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        if len(arr) == 0:
            return []
        else:
            temp_array = sorted(set(arr))
            hashmap = {}

            for i in range(len(temp_array)):
                hashmap[temp_array[i]] = i + 1

            for j in range(len(arr)):
                rank = hashmap[arr[j]]
                arr[j] = rank

            return arr

        # Time Complexity: O(n*log(n)), Space Complexity: O(n)
