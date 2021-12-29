class Solution:

    # https://leetcode.com/problems/find-right-interval/

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # brute force is o(n)^2 not worth it lets try to use binary search but
        # we need the index so lets construct new array and sort that array but we will
        # store original index of that

        sorted_array = sorted([[interval[0], index] for index, interval in enumerate(intervals)])
        answer = []

        for interv in intervals:
            target = interv[1]
            start = 0
            end = len(intervals)

            while start < end:
                mid = start + (end - start) // 2

                if sorted_array[mid][0] < target:
                    start = mid + 1
                else:
                    end = mid

            if start == len(intervals):
                answer.append(-1)
            else:
                answer.append(sorted_array[start][1])
        return answer

    # Time Complexity: O(n(logn)) Space Complexity: O(n)
