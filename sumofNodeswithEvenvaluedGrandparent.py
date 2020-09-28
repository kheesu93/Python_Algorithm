# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        tree = [root]
        grandCh = []
        totSum = 0
        while tree:
            ch = []
            parent = tree

            for cur in parent:
                if cur.val % 2 == 0:
                    for child in [cur.left, cur.right]:
                        if child:
                            ch.append(child)
                            for grand in [child.left, child.right]:
                                if grand:
                                    grandCh.append(grand.val)
                else:
                    for child in [cur.left, cur.right]:
                        if child:
                            ch.append(child)

            tree = ch

        for i in grandCh:
            totSum += i

        return totSum