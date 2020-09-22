# 1476. Subrectangle Queries
# https://leetcode.com/problems/subrectangle-queries/

from typing import List
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.matrix[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]

#["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
#[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]

input = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
obj = SubrectangleQueries(input)
print(obj.getValue(0,2))
print(obj.updateSubrectangle(0,0,3,2,5))
print(obj.getValue(0,2))
print(obj.getValue(3,1))
print(obj.updateSubrectangle(3,0,3,2,10))
print(obj.getValue(3,1))
print(obj.getValue(0,2))