"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 不是太明白    

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        
        if not root or root == A or root == B:
            return root

        # Divide
        left = self.lowestCommonAncestor(root.left, A, B) # 左边是不是有 A 或 B 其中的一个或多个
        right = self.lowestCommonAncestor(root.right, A, B) # 右边是不是有 A 或 B 其中的一个或多个
        
        # Conquer
        if left and right:
            return root
            
        if left:
            return left
            
        if right:
            return right
            
        return None
