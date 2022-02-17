from collections import defaultdict
from typing import List, Any


class Solution:

    # https://leetcode.com/problems/group-anagrams/

    def groupAnagrams(self, x: List[str]) -> List[list, Any]:

        Hashmap = defaultdict(list)

        for s in x:

            count_alpa = [0] * 26

            for char in s:
                count_alpa[ord(char) - ord("a")] += 1

            Hashmap[tuple(count_alpa)].append(s)

        return list(Hashmap.values())

    # Time Complexity: O(m*n), Space Complexity: O(n)
