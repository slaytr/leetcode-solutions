#problem 979
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        # 1 <= N <= 100 nodes
        # 0 <= node.val <= N
        '''
        if root does not have subtrees return 0
        if root only have left subtree then = distribute(root.left) + abs(root.left.val - 1), we need to change the root.val
        if root only have right subtree then = distribute(root.right) + abs(root.right.val - 1), we need to change the root.val
        if root have both left and right subtree then
        distributeCoins(root) = distribute(root.left) + distribute(root.right) + abs(root.left.val - 1) + abs(root.right.val - 1), we need to change the root.val
        '''
        
        if not root.left and not root.right:
            return 0
        elif root.left and not root.right:
            ans = self.distributeCoins(root.left) + abs(root.left.val - 1)
            root.val += root.left.val - 1
        elif not root.left and root.right:
            ans = self.distributeCoins(root.right) + abs(root.right.val - 1)
            root.val += root.right.val -1
        else:
            ans = self.distributeCoins(root.right) + abs(root.right.val - 1) + self.distributeCoins(root.left) + abs(root.left.val - 1)
            root.val += root.left.val -1 + root.right.val -1
        return ans