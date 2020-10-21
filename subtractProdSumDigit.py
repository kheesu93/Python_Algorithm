# 1281. Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0

        for digit in str(n):
            prod *= int(digit)
            summ += int(digit)

        return prod - summ