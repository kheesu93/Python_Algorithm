# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        result = []

        for num in nums:
            # count = 0

            temp = [j for j in nums if j < num]
            # for j in nums:
            #    if num > j:
            #        count += 1

            result.append(len(temp))

        return result