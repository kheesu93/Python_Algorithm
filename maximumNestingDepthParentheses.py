# 1614. Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        sList  = list(s)
        currentNest = 0
        result = []

        # max 함수로 비교
        #ans = 0

        for value in sList:
            if value == '(':
                currentNest += 1
            elif value == ')':
                currentNest -= 1
            #ans = max(currentNest,ans)
            result.append(currentNest)

        print(max(result))
        #return max(result)



s = "(1+(2*3)+((8)/4))+1"
sol = Solution()
sol.maxDepth(s)
