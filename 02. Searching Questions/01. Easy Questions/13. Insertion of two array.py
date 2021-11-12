class Solution:

    # https://leetcode.com/problems/intersection-of-two-arrays/

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        answer = []

        for i in nums1:
            if i in nums2:
                if i not in answer:
                    answer.append(i)

        return answer

    #  Time complexity: O(n), space Complexity: O(1)
