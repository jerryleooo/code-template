"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Non Recursion

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        
        if not root:
            return []
        
        stack = []
        preorder = []
        
        stack.append(root)
        
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return preorder

# Traverse

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        
        result = []
        
        def traverse(root):
            
            if not root:
                return
            
            result.append(root.val)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        print result
        return result

# Divide & Conquer

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        
        result = []
        
        if not root:
            return []
            
        # Divide
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        # Conquer
        result.append(root.val)
        result.extend(left)
        result.extend(right)
        
        return result