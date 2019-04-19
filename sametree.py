#Problem 100 - Same Tree
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        elif p == None and q == None:
            return True
        else:
            if p.val != q.val:
                return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
