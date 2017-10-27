"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 返回两个值

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        
        def helper(root):
            if not root:
                return True, 0
            
            left_is_balanced, left_depth = helper(root.left)
            right_is_balanced, right_depth = helper(root.right)
            
            if left_is_balanced and right_is_balanced and abs(left_depth - right_depth) <= 1:
                return True, max(left_depth, right_depth) + 1

            return False, -1
            
        is_balanced, depth = helper(root)
        return is_balanced

# 返回一个值

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        
        def max_depth(root):
            if not root:
                return 0
                
            left = max_depth(root.left)
            right = max_depth(root.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1
            
        return max_depth(root) != -1