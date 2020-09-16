# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        x = nums[:n]
        y = nums[n:]

        for i in range(n):
            answer.append(x[i])
            answer.append(y[i])

        return answer