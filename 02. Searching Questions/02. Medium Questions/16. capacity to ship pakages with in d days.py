class Solution:

    # https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        start = 1
        end = sum(weights)
        answer = float('inf')

        while start <= end:

            mid = start + (end - start) // 2
            block_weight = 0
            days_needed = 0
            impossible_task = False

            for i in weights:
                if i > mid:
                    impossible_task = True
                    break
                elif (block_weight + i) > mid:
                    block_weight = 0
                    days_needed += 1
                    block_weight += i
                else:
                    block_weight += i
            days_needed += 1

            if impossible_task:
                start = mid + 1
            elif days_needed == days:
                answer = min(answer, mid)
                end = mid - 1
            elif days_needed > days:
                start = mid + 1
            else:
                answer = min(answer, mid)
                end = mid - 1

        return answer

    # Time Complexity: O(n * log(n)), Space Complexity: O(1)
