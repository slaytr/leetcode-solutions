#Problem 965
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        if root.left == None and root.right == None:
            return True
        elif root.left == None and root.right != None:
            if root.right.val != root.val:
                return False
        elif root.left != None and root.right == None:
            if root.left.val != root.val:
                return False
        elif root.left.val != root.val or root.right.val != root.val:
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            