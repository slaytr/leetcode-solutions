#Problem 94

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.list = []
        
        self.traverse(root)
        
        return self.list
    
    def traverse(self, root):
        if root:
            self.traverse(root.left)
            
            self.list.append(root.val)
            
            self.traverse(root.right)