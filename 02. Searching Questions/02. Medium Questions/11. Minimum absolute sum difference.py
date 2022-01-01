class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:

        sorted_array_1 = sorted(nums1)
        total = 0
        for i in range(len(nums1)):
            total += abs(nums1[i] - nums2[i])

        answer = total

        for x, y in zip(nums1, nums2):

            current_difference = abs(x - y)

            idx = self.binary_search(sorted_array_1, y)

            if 0 <= idx < len(sorted_array_1):
                val = abs(sorted_array_1[idx] - y)
                pd = total - current_difference + val
                answer = min(answer, pd)

            if idx - 1 < len(sorted_array_1):
                val = abs(sorted_array_1[idx - 1] - y)
                pd = total - current_difference + val
                answer = min(answer, pd)

        return answer % (10 ** 9 + 7)

    def binary_search(self, array, target):

        start, end = 0, len(array) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if array[mid] == target:
                return mid
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start

    # Time Complexity: O(n*logn), Space Complexity: O(n)
