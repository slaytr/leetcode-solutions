
class Solution(object):
    def diameterOfBinaryTree(self, root):
        m = [0]
        
        def helper(root):
            if not root:
                return 0
            else:
                left_height = helper(root.left)
                right_height = helper(root.right)
                m[0] = max(m[0], left_height + right_height)

                return (max(left_height, right_height)+1)
        
        helper(root)
        
        return m[0]