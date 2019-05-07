#Problem 589. N-ary Tree Preorder Traversal
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            self.preorder = []
            self.trav(root)
            return self.preorder
        else:
            return []

    def trav(self, node):
        if node:
            self.preorder.append(node.val)
            if node.children:
                for child in node.children:
                    self.trav(child)