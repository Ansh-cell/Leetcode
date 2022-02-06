class Solution:

    # https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target == arr

    # Time Complexity: O(n*log(n)), Space Complexity: O(1)
