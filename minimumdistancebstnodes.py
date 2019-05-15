#Brute Force
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.vals = []
        self.min = 999999999
        if root:
            self.trav(root)
            for i in range(len(self.vals)):
                for j in range(i+1, len(self.vals)):
                    if abs(self.vals[i]-self.vals[j]) < self.min:
                        self.min =  abs(self.vals[i]-self.vals[j])
            return self.min
                    
    def trav(self, node):
        if node:
            self.vals.append(node.val)
            self.trav(node.left)
            self.trav(node.right)