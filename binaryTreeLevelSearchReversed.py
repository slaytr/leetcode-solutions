# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.queue = [(root,0)]
        self.res = []
        self.max = 0
        self.find_depth(root, 0)
        self.res = [[] for i in range(self.max+1)]
        self.recurse(root)
        self.rev = []
        for index, l in enumerate(self.res):
            if index % 2 != 0:
                self.rev.append(list(reversed(l)))
            else:
                self.rev.append(l)
        return self.rev
    
    def find_depth(self, node,depth):
        if node:
            self.max = max(self.max, depth)
            self.find_depth(node.left, depth +1)
            self.find_depth(node.right, depth +1)
            
    def recurse(self, node):
        if node:
            self.res[self.queue[0][1]].append(node.val)

            if node.left:
                self.queue.append((node.left, self.queue[0][1]+1))
            if node.right:
                self.queue.append((node.right, self.queue[0][1]+1))
            self.queue.pop(0)
            if self.queue:
                self.recurse(self.queue[0][0])
            
        