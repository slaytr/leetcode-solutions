# Problem 872 - Leaf-Similar Trees

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        self.list = []
        self.recurseTree(root1)
        
        self.list2 = self.list
        self.list = []
        self.recurseTree(root2)
        return self.list2 == self.list
        
    def recurseTree(self, node):
        if node:
            if node.left == None and node.right == None:
                self.list.append(node.val)
            else:
                self.recurseTree(node.left)
                self.recurseTree(node.right)