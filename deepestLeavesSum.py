# Definition for a binary tree node.
import null as null


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        tree = [root]
        a = 0

        while tree:
            ch = []
            pre = tree

            for cur in tree:
                for child in [cur.left, cur.right]:
                    if child:
                        ch.append(child)
            tree = ch

        for leaf in pre:
            a += leaf.val

        return a


root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
s = Solution()
s.deepestLeavesSum(root)