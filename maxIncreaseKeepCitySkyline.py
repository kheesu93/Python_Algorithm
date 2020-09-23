# 807. Max Increase to Keep City Skyline
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        lrmax = [max(row) for row in grid]
        # [8,7,9,3]
        udmax = [max(col) for col in zip(*grid)]
        # [9,4,8,7]

        diff = 0

        for i, row in enumerate(grid):
            # 0:3,0,8,4 / 1:2,4,5,7 / 2:9,2,6,3 / 3:0,3,1,0
            for j, col in enumerate(row):
                limit = min(lrmax[i],udmax[j])
                diff += max(limit-col, 0)

        return diff



grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

s = Solution()
s.maxIncreaseKeepingSkyline(grid)


#[ [3, 0, 8, 4],
#  [2, 4, 5, 7],
#  [9, 2, 6, 3],
#  [0, 3, 1, 0] ]

#The skyline viewed from top or bottom is: [9, 4, 8, 7]
#The skyline viewed from left or right is: [8, 7, 9, 3]

#The grid after increasing the height of buildings without affecting skylines is:

#gridNew = [ [8, 4, 8, 7],
#            [7, 4, 7, 7],
#            [9, 4, 8, 7],
#            [3, 3, 3, 3] ]