# 1395. Count Number of Teams
# https://leetcode.com/problems/count-number-of-teams/

from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i, ivalue in enumerate(rating):
            for j, jvalue in enumerate(rating[i+1:]):
                #if ivalue < jvalue:
                for k, kvalue in enumerate(rating[i+j+1:]):
                        if ivalue < jvalue < kvalue:
                            count += 1
                #elif ivalue > jvalue:
                    #for k, kvalue in enumerate(rating[i+j+1:]):
                        elif ivalue> jvalue > kvalue:
                            count += 1

        return count

rating = [4,7,9,5,10,8,2,1,6]

s = Solution()
print(s.numTeams(rating))