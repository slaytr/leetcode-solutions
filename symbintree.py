class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        def f(n1, n2):
            
            if not n1 and not n2:
                return True
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                return f(n1.left, n2.right) & f(n1.right, n2.left)
            else:
                return False
            
        return f(root.left, root.right)