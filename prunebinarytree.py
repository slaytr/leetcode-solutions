class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def prune(node):
            if node:
                if not node.left and not node.right and node.val == 0:
                    return False
                else:
                    if prune(node.left) == False:
                        node.left = None
                    if prune(node.right) == False:
                        node.right = None
                    if not node.left and not node.right and node.val == 0:
                        return False
        prune(root)
        return root