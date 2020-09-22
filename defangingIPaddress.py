# 1108. Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")

address = "1.1.1.1"
s = Solution()
print(s.defangIPaddr(address))