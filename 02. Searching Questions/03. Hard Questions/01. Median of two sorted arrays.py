class Solution:

    # https://leetcode.com/problems/median-of-two-sorted-arrays/

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        final_array = sorted(nums1 + nums2)

        if len(final_array) % 2 != 0:
            start = 0
            end = len(final_array) - 1

            mid = start + (end - start) // 2

            return final_array[mid]
        else:
            start = 0
            end = len(final_array) - 1

            mid = start + (end - start) // 2

            answer = (final_array[mid] + final_array[mid + 1]) / 2
            return answer

        # Time Complexity: O(n * log(n)), Space Complexity: O(nums1 + nums2)

        # It's not optimised
