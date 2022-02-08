import collections


class Solution:

    # https://leetcode.com/problems/sort-array-by-increasing-frequency/

    def frequencySort(self, nums: List[int]) -> List[int]:
        s = collections.Counter(nums)
        nums.sort(key=lambda x: (s[x], -x))
        return nums

    # Time Complexity: O(n*log(n)), Space Complexity: O(1)
