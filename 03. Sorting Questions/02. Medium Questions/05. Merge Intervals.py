from operator import itemgetter


class Solution:

    # https://leetcode.com/problems/merge-intervals/

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        hashmap = {}
        answer = []
        intervals.sort(key=itemgetter(0))
        for i in intervals:
            key = i[0]
            end = i[1]
            value = i

            if key in hashmap:
                if hashmap[key][1] <= end:
                    hashmap[key][1] = end
            else:
                hashmap[key] = value
        for i in intervals:
            intial_start = i[0]
            start = i[0]
            end = i[1]
            if len(answer) >= 1 and start >= answer[-1][0] and end <= answer[-1][1]:
                continue
            while start <= end:
                if start in hashmap:
                    if end <= hashmap[start][1]:
                        end = hashmap[start][1]
                    start += 1
                else:
                    start += 1
            answer.append([intial_start, end])

        return answer
