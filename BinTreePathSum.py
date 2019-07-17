# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        self.sum = sum
        self.hasSum = False
        self.sumPath(root, 0)
        return self.hasSum
        
    def sumPath(self, node, total):
        if node:
            total = total + node.val
            self.sumPath(node.left, total)
            self.sumPath(node.right, total)
            if not node.left and not node.right and total == self.sum:
                self.hasSum = True