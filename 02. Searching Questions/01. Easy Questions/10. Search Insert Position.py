class Solution:

    # https://leetcode.com/problems/search-insert-position/submissions/

    def searchInsert(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while start < end:

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if nums[start] < target:
            return start + 1
        else:
            return start