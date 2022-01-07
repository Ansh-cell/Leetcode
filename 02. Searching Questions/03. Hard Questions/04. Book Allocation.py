class Solution:

    # search: Allocate minimum number of pages : geeksforgeeks

    # Function to find minimum number of pages.
    def findPages(self, A, N, m):
        # code here
        if m == 1:
            return sum(A)
        elif N == m:
            return max(A)
        else:
            start = 0
            end = 0
            for i in A:
                end += i
                if i > start:
                    start = i

            answer = float('inf')
            while start < end:

                mid = int(start + (end - start) // 2)
                pieces = 0
                pieces_sum = 0
                for i in range(N):

                    if pieces_sum + A[i] > mid:
                        pieces += 1
                        pieces_sum = 0
                        pieces_sum += A[i]
                    else:
                        pieces_sum += A[i]
                pieces += 1

                if pieces <= m:
                    end = mid
                else:
                    start = mid + 1

            return start

        # Time Complexity: O(N * log(N)), Space Complexity: O(1)
