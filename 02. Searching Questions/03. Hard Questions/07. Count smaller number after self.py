from sortedcontainers import SortedList
from bisect import bisect_left


class Solution:

    # https://leetcode.com/problems/count-of-smaller-numbers-after-self/

    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        sorted_list = SortedList()

        for i in range(len(nums) - 1, -1, -1):
            indx = sorted_list.bisect_left(nums[i])
            ans.append(indx)
            sorted_list.add(nums[i])

        return ans[::-1]

    # Time Complexity: O(n * log(m)), Space Complexity: O(n)    n: nums, m: sorted_list
