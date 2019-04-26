#Problem 606
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        self.string = ""
        self.traverseTree(t)
        return self.string[1:-1]
    
    def traverseTree(self, root):
        if root:
            self.string = self.string + "({}".format(root.val)
            if root.left:
                self.traverseTree(root.left)
            elif root.right:
                self.string = self.string + "()"
            self.traverseTree(root.right)
            self.string = self.string + ")"
        