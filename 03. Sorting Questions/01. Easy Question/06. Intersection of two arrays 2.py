class Solution:

    # https://leetcode.com/problems/intersection-of-two-arrays-ii/

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        answer = []

        for i in nums2:

            if self.binary_search(i, nums1):
                answer.append(i)

        return answer

    def binary_search(self, target, array):
        start = 0
        end = len(array) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if array[mid] == target:
                array.pop(mid)
                return True
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False
