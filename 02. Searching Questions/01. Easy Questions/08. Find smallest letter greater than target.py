class Solution:

    # https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        start = 0
        end = len(letters) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1

        if start == len(letters):
            return letters[0]
        return letters[start]

        # Time Complexity: O(log(n)), Space Complexity: O(1)
