# Problem 226 - Invert Binary Tree
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.stack = []
        self.recurseTree(root)
        return root
    
    def recurseTree(self, root):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.recurseTree(root.left)
            self.recurseTree(root.right)