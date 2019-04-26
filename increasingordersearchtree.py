# Problem 897

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.stack = []
        self.add_stack(root)
        first = True
        root = None
        prev = None
        node = None

        for index in range(len(self.stack)):
            if not first:
                prev = node
           
            node = TreeNode(self.stack[index])
            
            if first:
                root = node
                first = False
            else:
                prev.right = node
                
        return root
        
    def add_stack(self, root):
        if root:
            self.add_stack(root.left)
            self.stack.append(root.val)
            self.add_stack(root.right)