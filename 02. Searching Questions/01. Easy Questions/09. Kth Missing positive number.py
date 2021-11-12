class Solution:

    # https://leetcode.com/problems/kth-missing-positive-number/submissions/

    def findKthPositive(self, arr: List[int], k: int) -> int:

        start = 0
        end = len(arr) - 1

        def Missing_values(index: int) -> int:
            return arr[index] - (index + 1)

        while start < end:

            mid = start + (end - start) // 2
            miss_val = Missing_values(mid)
            if miss_val < k:
                start = mid + 1
            else:
                end = mid - 1
        check_for_result = Missing_values(start)
        if check_for_result < k:
            return arr[start] + (k - check_for_result)
        else:
            return arr[start] + (k - check_for_result) - 1
