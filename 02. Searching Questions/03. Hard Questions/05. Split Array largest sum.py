class Solution:

    # https://leetcode.com/problems/split-array-largest-sum/

    def splitArray(self, nums: List[int], m: int) -> int:
        if m == 1:
            return sum(nums)
        elif len(nums) == m:
            return max(nums)
        else:
            start = 0
            end = 0
            for i in nums:
                end += i
                if i > start:
                    start = i

            answer = float('inf')
            while start < end:

                mid = int(start + (end - start) // 2)
                pieces = 0
                pieces_sum = 0
                for i in range(len(nums)):

                    if pieces_sum + nums[i] > mid:
                        pieces += 1
                        pieces_sum = 0
                        pieces_sum += nums[i]
                    else:
                        pieces_sum += nums[i]
                pieces += 1

                if pieces <= m:
                    end = mid
                else:
                    start = mid + 1

            return start

    # Time Complexity: O(n * log(n)), Space Complexity: O(1)
