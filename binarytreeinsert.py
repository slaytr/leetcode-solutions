#Problem 701 - Recursive Solution ~5min
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root != None:
            if val > root.val:
                if root.right == None:
                    root.right = TreeNode(val)
                else:
                    self.insertIntoBST(root.right, val)
            elif val < root.val:
                if root.left == None:
                    root.left = TreeNode(val)
                else:
                    self.insertIntoBST(root.left, val)
        return root
