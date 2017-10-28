"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

# 用 template 轻松解决

import Queue

class Solution:
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        # write your code here

        queue = Queue.Queue()
        queue.put(s)
        visited = set()
        
        while not queue.empty():
            for i in range(queue.qsize()):
                node = queue.get()
                if node in visited:
                    continue
                if node == t:
                    return True

                visited.add(node)
                for n in node.neighbors:
                    queue.put(n)
        return False
                