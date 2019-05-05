# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0
        self.node_vals = []
        self.getTotal(root)
        
        self.node_vals = sorted(self.node_vals)
        self.changeVal(root)
        
        return root
        
    def getTotal(self, node):
        if node:
            self.total += node.val
            self.node_vals.append(node.val)
            self.getTotal(node.left)
            self.getTotal(node.right)
    
    def changeVal(self, node):
        if node:
            dif = 0
            for value in self.node_vals:
                if value >= node.val:
                    break
                dif += value
            node.val = self.total - dif
            self.changeVal(node.left)
            self.changeVal(node.right)
            
            