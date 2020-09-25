# 1282. Group the People Given the Group Size They Belong To
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from typing import List
from collections import defaultdict
# import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        key = defaultdict(list)
    ### Dic & setDefault
        #key = {}
        result = []

        for i, gSize in enumerate(groupSizes):
            # if gSize not in key:
            #    key[gSize] = []
            # key.setdefault(gSize,[])
            key[gSize].append(i)
            if len(key[gSize]) == gSize:
                result.append(key[gSize])
                key[gSize] = []

        return result


groupSizes = [3,3,3,3,3,1,3]
s = Solution()
s.groupThePeople(groupSizes)