# Problem 654 - Was fun
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # Create Root Node
        max_val = max(nums)
        node = TreeNode(max_val)
        left_array = nums[:nums.index(max_val)]
        right_array = nums[nums.index(max_val)+1:]
        
        # Create children nodes then create subtrees for them
        if len(left_array) > 0:        # Python Max() requires array to be not empty
            node.left = TreeNode(max(left_array))
            self.createSubtree(left_array, node.left)
        else:
            node.left = None
        if len(right_array) > 0:
            node.right = TreeNode(max(right_array))
            self.createSubtree(right_array, node.right)
        else:
            node.right = None
        return node
        
    def createSubtree(self, array, node):
        if len(array) == 1:
            max_val = array[0]
        elif len(array) > 1:
            max_val = max(array)
            left_construct = True
            right_construct = True
            
            # if node is left most or right most
            if array.index(max_val) == 0:
                node.left = None
                left_construct = False
            if array.index(max_val) == (len(array)-1):
                node.right = None
                right_construct = False

            if left_construct == True:
                left_array = array[:array.index(max_val)]
                node.left = TreeNode(max(left_array))
                self.createSubtree(left_array, node.left)
            if right_construct == True:
                right_array = array[array.index(max_val)+1:]
                node.right = TreeNode(max(right_array))
                self.createSubtree(right_array, node.right)

        

        