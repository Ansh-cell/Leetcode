# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:

    # https://leetcode.com/problems/find-in-mountain-array/

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        peak_idx = self.peak_index(mountain_arr)
        search_on_left = self.algostic_binary(True, mountain_arr, 0, peak_idx, target)
        if search_on_left != -1:
            return search_on_left
        else:
            return self.algostic_binary(False, mountain_arr, peak_idx + 1, mountain_arr.length() - 1, target)

    def peak_index(self, arr):
        start = 0
        end = arr.length() - 1
        while start < end:

            mid = int(start + (end - start) // 2)

            if arr.get(mid) > arr.get(mid + 1):
                end = mid
            else:
                start = mid + 1
        return start

    def algostic_binary(self, check, arr, start, end, target):

        start = start
        end = end

        while start <= end:

            mid = int(start + (end - start) // 2)

            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) > target:
                if check:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if check:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

    # Time Complexity: O(log(n)), Space Complexity: O(1)
