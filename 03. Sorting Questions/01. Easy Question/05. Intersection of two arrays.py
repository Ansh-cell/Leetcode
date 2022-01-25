class Solution:

    # https://leetcode.com/problems/intersection-of-two-arrays/

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        largest_array = 0
        smallest_array = 0
        if len(nums1) >= len(nums2):
            largest_array = nums1
            smallest_array = nums2
        else:
            largest_array = nums2
            smallest_array = nums1

        for i in range(len(largest_array)):
            if largest_array[i] in smallest_array and largest_array[i] not in answer:
                answer.append(largest_array[i])

        return answer

    # Time Complexity: O(n^2), Space Complexity: O(n): if we include our answer otherwise O(1)


# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         Hash_set = set()
#         Hash_intersection = set()
#         for i in nums1:
#             Hash_set.add(i)
#         for j in nums2:
#             if j in Hash_set:
#                 Hash_intersection.add(j)
#
#         return list(Hash_intersection)

    # Time Complexity: O(n), Space Complexity: O(n^2)
