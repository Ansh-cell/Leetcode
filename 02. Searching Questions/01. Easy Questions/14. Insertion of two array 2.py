class Solution:

    # https://leetcode.com/problems/intersection-of-two-arrays-ii/

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        HashSet = set()
        Intersection = []

        for i in nums1:  # O(n)
            HashSet.add(i)

            # i = (1,2)

        for j in nums2:  # O(m)

            if j in HashSet:  # O(1)
                Intersection.append(j)
                HashSet.remove(j)
                nums1.remove(j)
            else:  # O(1)
                if j in nums1:
                    Intersection.append(j)
                    nums1.remove(j)

        return Intersection

        # Overall Time Complexity = O(n + m)