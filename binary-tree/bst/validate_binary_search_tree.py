"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Divide and Conqer

class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        
        def helper(root):
            if not root:
                return True, float('-inf'), float('inf')
            
            left_is_bst, left_max_value, left_min_value = helper(root.left)
            right_is_bst, right_max_value, right_min_value = helper(root.right)
            
            if not left_is_bst or not right_is_bst:
                return False, 0, 0
                
            if root.left and left_max_value >= root.val or root.right and right_min_value <= root.val:
                return False, 0, 0
                
            return True, max(root.val, right_max_value), min(root.val, left_min_value)

        is_bst, max_value, min_value = helper(root)
        return is_bst

# Another Divide and Conquer

class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        
        def helper(root, min_value, max_value):
            if not root:
                return True
                
            if root.val <= min_value or root.val >= max_value:
                return False
                
            return (helper(root.left, min_value, min(max_value, root.val)) and 
                    helper(root.right, max(min_value, root.val), max_value))
        
        return helper(root, float('-inf'), float('inf'))