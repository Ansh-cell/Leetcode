class Solution:

    # https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        hashmap = {}
        new_array = nums.copy()
        new_array.sort()

        for i in range(len(new_array)):
            if new_array[i] not in hashmap:
                hashmap[new_array[i]] = i

        for i in range(len(nums)):
            val = nums[i]
            new_array[i] = hashmap[val]

        return new_array

    # Time Complexity: O(n*log(n)), Space Complexity: O(n)
