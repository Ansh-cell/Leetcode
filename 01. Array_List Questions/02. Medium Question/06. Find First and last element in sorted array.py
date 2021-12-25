class Solution:

    # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first_index = self.binary_search(nums, target, True)
        second_index = self.binary_search(nums, target, False)

        return first_index, second_index

    def binary_search(self, array, target, check_side):
        answer = -1
        start = 0
        end = len(array) - 1
        left_check_side = check_side

        while start <= end:

            mid = start + (end - start) // 2

            if array[mid] == target:
                answer = mid

                if left_check_side:
                    end = mid - 1
                else:
                    start = mid + 1
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return answer

    # Time Complexity: O(log(n)), Space Complexity: O(1)
