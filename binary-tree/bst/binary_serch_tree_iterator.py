"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        self.curt = root
        
    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here

        return self.curt or self.stack

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        while self.curt:
            self.stack.append(self.curt)
            self.curt = self.curt.left

        self.curt = self.stack.pop()
        node = self.curt
        self.curt = self.curt.right

        return node