class Solution:

    # https://leetcode.com/problems/relative-sort-array/

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = {}
        answer = []
        diff = []

        for val in arr2:
            hashmap[val] = 0

        for val in arr1:
            if val not in hashmap:
                diff.append(val)
            else:
                hashmap[val] += 1

        for key, value in hashmap.items():
            answer.extend([key for _ in range(value)])

        answer.extend(sorted(diff))
        return answer

    # Time Complexity: O(n^2), Space Complexity: O(n)
