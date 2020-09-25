# Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/submissions/

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            answer.append(sum(nums[0:i + 1]))

        return answer
    #runningSum
