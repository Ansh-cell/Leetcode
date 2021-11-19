class Solution:

    # https://leetcode.com/problems/flipping-an-image/

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            i = 0
            j = len(image[i]) - 1
            while i < j:
                if image[row][i] == 1:
                    image[row][i] = 0
                else:
                    image[row][i] = 1
                if image[row][j] == 1:
                    image[row][j] = 0
                else:
                    image[row][j] = 1

                image[row][j], image[row][i] = image[row][i], image[row][j]
                i += 1
                j -= 1
            if i == j:
                if image[row][i] == 1:
                    image[row][i] = 0
                else:
                    image[row][i] = 1

        return image

    # Time Complexity: O(n^2), Space Complexity: O(1)
