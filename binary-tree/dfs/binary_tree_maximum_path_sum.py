"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        
        def helper(root):
            if not root:
                return 0, -float('inf')
                
            # Divide
            left_single_path, left_max_path = helper(root.left)
            right_single_path, right_max_path = helper(root.right)
            
            # Conquer
            single_path = max(left_single_path, right_single_path) + root.val
            single_path = max(single_path, 0)
            
            max_path = max(left_max_path, right_max_path)
            max_path = max(max_path, left_single_path + right_single_path + root.val)
            
            return single_path, max_path
            
        single_path, max_path = helper(root)
        return max_path

