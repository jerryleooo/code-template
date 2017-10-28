"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import Queue

class Solution:
    """
    @param: root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        
        if not root:
            return []
            
        result = []
        queue = Queue.Queue()
        
        queue.put(root)
        
        while not queue.empty():
            level = []
            for i in range(queue.qsize()):
                node = queue.get()
                level.append(node.val)

                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
                    
            result.append(level)
            
        return result