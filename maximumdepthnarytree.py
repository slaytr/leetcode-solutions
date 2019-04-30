class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.maxes = []
        self.travel(root, 0)
        if len(self.maxes) > 0:
            return max(self.maxes)
        else:
            return 0
    
    def travel(self, root, count):
        if root:
            count += 1
            for i in root.children:
                self.travel(i, count)
            if len(root.children) == 0:
                self.maxes.append(count)