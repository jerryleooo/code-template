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
    @param: root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        
        if not root:
            return []
            
        result = []
            
        queue = Queue.Queue()
        queue.put(root)
        
        round = 0
        
        while not queue.empty():
            level = []
            for i in range(queue.qsize()):
                node = queue.get()

                if round % 2 == 0:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                    
                if node.left:
                    queue.put(node.left)
                    
                if node.right:
                    queue.put(node.right)
                
            round += 1
                    
            result.append(level)
            
        return result