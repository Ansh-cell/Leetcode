class Solution:

    # https://leetcode.com/problems/count-items-matching-a-rule/

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        return self.check_maching(items, ruleKey, ruleValue)

    def check_maching(self, items, rulekey, rulevalue):

        count = 0

        if rulekey == 'type':

            for i in range(len(items)):

                if items[i][0] == rulevalue:
                    count += 1
        elif rulekey == 'color':

            for i in range(len(items)):

                if items[i][1] == rulevalue:
                    count += 1
        else:

            for i in range(len(items)):

                if items[i][2] == rulevalue:
                    count += 1

        return count

    # Time Complexity: O(n), Space Complexity: O(1)
