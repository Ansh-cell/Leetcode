class Solution:

    # https://leetcode.com/problems/check-if-n-and-its-double-exist/

    def checkIfExist(self, arr: List[int]) -> bool:

        for i in range(len(arr)):  # O(n^2)
            double_number = arr[i] * 2
            if arr[i] == double_number:
                if double_number in arr[i + 1:]:
                    return True
                else:
                    if double_number in arr[:i]:
                        return True
            else:
                if double_number in arr:
                    return True
        return False

    # Space Complexity: O(1)
