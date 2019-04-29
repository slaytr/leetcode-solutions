class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0
        L, R = sorted([L, R])
        self.traverseTree(root, L, R)
        return self.sum
    
    def traverseTree(self, root, L, R):
        if root:
            if root.val >= L and root.val <= R:
                self.sum += root.val
            self.traverseTree(root.left, L, R)
            self.traverseTree(root.right, L, R)    
        
# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:        
#         self.nrange = []
#         self.traverseTree(root)
#         return sum(self.nrange[self.nrange.index(L): self.nrange.index(R)+1])
        
#     def traverseTree(self, root):
#         if root:
#             self.traverseTree(root.left)
#             self.nrange.append(root.val)
#             self.traverseTree(root.right)