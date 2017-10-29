# -*- coding: utf-8 -*-

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

# Traverse

class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: 
    """
    
    last_node = None
    
    def flatten(self, root):
        # write your code here
        if not root:
            return
        
        if self.last_node:
            self.last_node.left = None
            self.last_node.right = root
            
        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)

# Divid & Conquer
# 这里的逻辑是无需用头，因为是已知的，只需要用尾巴

class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: 
    """
    
    def flatten(self, root):
        
        def helper(root):
            if not root:
                return None
                
            left_last = helper(root.left)
            right_last = helper(root.right)
            
            if left_last:
                left_last.right = root.right
                root.right = root.left
                root.left = None
            
            if right_last:
                return right_last
                
            if left_last:
                return left_last
                
            return root
        
        helper(root)

# Non-Recursion
# 我觉得是很好的 dfs 模板

class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: 
    """
    
    def flatten(self, root):
        if not root:
            return
        
        stack = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
                
            node.left = None
            
            if stack:
                node.right = stack[-1]
            else:
                node.right = None