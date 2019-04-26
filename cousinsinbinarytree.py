#Problem 993
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x = x
        self.y = y
        self.dict = dict()
        self.bool = True
        
        self.recurseTree(root, 0)
        
        if not self.bool:
            return self.bool
        print(self.dict)
        
        if x in self.dict.keys() and y in self.dict.keys():
            if self.dict[x] == self.dict[y]:
                return True
            else:
                return False
        
    def recurseTree(self, node, depth):
        if node:
            if node.right and node.left:
                if node.right.val == self.x and node.left.val == self.y:
                    self.bool = False
                if node.left.val == self.x and node.right.val == self.y:
                    self.bool = False
            self.dict[node.val] = depth
            self.recurseTree(node.left, depth+1)
            self.recurseTree(node.right, depth+1)