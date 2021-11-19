class Solution:

    # https://leetcode.com/problems/shuffle-the-array/

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [0] * len(nums)
        index = 0

        for i in range(int(len(nums) / 2)):
            arr[index] = nums[i]
            arr[index + 1] = nums[int(len(nums) / 2 + i)]
            index += 2
        return arr

    # Time Complexity: O(n), Space Complexity: O(n)
