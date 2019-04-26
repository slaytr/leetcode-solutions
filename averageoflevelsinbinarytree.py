#Problem 637 Average of Levels in Binary Tree
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level = 0
        self.count = []
        self.levels = {}
        self.recurseTree(root, level)
        results = []
        for key in self.levels:
            results.append(self.levels[key]/self.count[key])
        return results
        
    def recurseTree(self, root, level):
        if root:
            if level not in self.levels.keys():
                self.levels[level] = root.val
                self.count.append(0)
            else:
                self.levels[level] += root.val
            self.count[level] += 1
            level +=1
            self.recurseTree(root.left, level)
            self.recurseTree(root.right, level)