#Problem 235
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.values = []
        self.p, self.q = sorted([p.val, q.val])
        self.traverseTree(root)
        return self.values[len(self.values)-1][0]
    
    def traverseTree(self, node):
        if node:
            self.traverseTree(node.left)
            self.traverseTree(node.right)
            if node.val >= self.p and node.val <= self.q: 
                self.values.append((node, node.val))
        