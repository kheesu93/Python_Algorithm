# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0

        for s in list(S):
            for j in list(J):
                if s == j:
                    count += 1

        print(count)
        return count

J = "aA"
S = "aAAbbbb"

s = Solution()
s.numJewelsInStones(J, S)