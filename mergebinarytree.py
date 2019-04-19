#Problem 617 - Solution is yuck
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if t1 == None and t2 != None:
            t3 = TreeNode(t2.val)
        elif t2 == None and t1 != None:
            t3 = TreeNode(t1.val)
        elif t1 == None and t2 == None:
            t3 = None
        else:
            #Main Node
            t3 = TreeNode(t1.val+t2.val)
        
            if t1.left == None:
                if t2.left != None:
                    t3.left = t2.left
                else:
                    t3.left = None
            else:
                if t2.left != None:
                    t3.left = self.mergeTrees(t1.left, t2.left)
                else:
                    t3.left = t1.left

            if t1.right == None:
                if t2.right != None:
                    t3.right = t2.right
                else:
                    t3.right = None
            else:
                if t2.right != None:
                    t3.right = self.mergeTrees(t1.right, t2.right)
                else:
                    t3.right = t1.right

        return t3