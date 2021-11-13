class Solution:

    # https://leetcode.com/problems/fair-candy-swap/

    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        # Alice: [1, 1] --> candy: 2
        # Bob: [2, 2] --> candy: 4
        # you have to exchange candy in such a way that both friend has equal number of candy
        # well its a simple math
        # Alice - x + y = Bob + x - y
        # x = number of candy alice send to bob
        # y = number of candy bob send to alice
        # find either x or y
        # 2x = alice - bob + 2y
        # x = (alice - bob) / 2 + y
        # if we find how much candy alice given to bob then we will found our answer

        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)

        setAlice = set(aliceSizes)  # space Complexity = O(n)  where n = size of alice_list

        for y in bobSizes:

            if (sum_alice - sum_bob) / 2 + y in setAlice:
                return [(sum_alice - sum_bob) / 2 + y, y]

        # Time Complexity: O(n + m)
