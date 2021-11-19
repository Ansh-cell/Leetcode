class Solution:

    # https://leetcode.com/problems/check-if-the-sentence-is-pangram/

    def checkIfPangram(self, sentence: str) -> bool:

        for i in range(26):

            if chr(97 + i) not in sentence:
                return False
        return True

    # Time Complexity: O(1), Space Complexity: O(1)
