class Solution:

    # https://leetcode.com/problems/contains-duplicate/

    def containsDuplicate(self, nums: List[int]) -> bool:
        length_with_duplicate = len(nums)  # O(n)
        length_without_duplicate = len(set(nums))  # O(n)
        return length_with_duplicate > length_without_duplicate

    # Time Complexity: O(n), Space Complexity: O(1)
