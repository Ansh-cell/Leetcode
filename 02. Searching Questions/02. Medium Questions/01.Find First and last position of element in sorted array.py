class Solution:

    # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first_position = self.binary_search(nums, target, True)
        second_position = self.binary_search(nums, target, False)
        return first_position, second_position

    def binary_search(self, arr, target, check_side):
        answer = -1
        start = 0
        end = len(arr) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if arr[mid] == target:
                answer = mid
                if check_side:  # This condition is to check on left side
                    end = mid - 1
                else:
                    start = mid + 1  # this condition is to check on right side
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return answer

    # Time Complexity: O(log(n)), Space Complexity: O(1)
