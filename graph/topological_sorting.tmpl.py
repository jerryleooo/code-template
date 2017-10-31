# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

import Queue
from collections import defaultdict

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        
        result = []
        indegrees = defaultdict(int)
        
        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1
                
        queue = Queue.Queue()
        for node in graph:
            if node not in indegrees:
                queue.put(node)
                result.append(node)
                
        while not queue.empty():
            node = queue.get()
            for n in node.neighbors:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    del indegrees[n]
                    queue.put(n)
                    result.append(n)
                    
        return result