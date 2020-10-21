# 1528. Shuffle String
# https://leetcode.com/problems/shuffle-string/

from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict = {indices[i]: s[i] for i in range(len(indices))}
        sDict = sorted(dict.keys())
        result = list(dict[j] for j in sDict)

        return ''.join(result)