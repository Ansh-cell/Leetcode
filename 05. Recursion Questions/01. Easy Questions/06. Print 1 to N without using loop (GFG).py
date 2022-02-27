class Solution:

    # Complete this function
    def printNos(self, N):
        # Your code here
        if N == 1:
            print(1, end=" ")
            return
        else:
            self.printNos(N - 1)
            print(N, end=" ")

    # Time Complexity: O(n), Space Complexity: O(n)
