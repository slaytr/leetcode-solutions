
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root:
            self.list = []

            self.trav(root)
            
            count = {}
            for i in self.list:
                if i not in count:
                    count[i] = 1
                else:
                    count[i] += 1
                    
            max_val = max(count.values())
            res = []
            for key in count:
                if count[key] == max_val:
                    res.append(key)
            return res
            
        else:
            return []

    def trav(self, node):
        if node:
            node.val = self.trav(node.left) + self.trav(node.right) + node.val
            self.list.append(node.val)
            return node.val
        return 0