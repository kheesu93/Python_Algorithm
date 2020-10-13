# 1614. Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        sList  = list(s)
        leftNest = 0
        rightNest = 0
        result = []

        for value in sList:
            if value == '(':
                leftNest += 1
            elif value == ')':
                rightNest -= 1
            result.append(leftNest + rightNest)

        print(result)
        return max(result)



s = "(1+(2*3)+((8)/4))+1"
sol = Solution()
sol.maxDepth(s)
