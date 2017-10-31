# -*- coding: utf-8 -*-

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here

        if not node:
            return None

        nodes_map = {node: UndirectedGraphNode(node.label)}
        nodes = [node]
        i = 0
        
        while i < len(nodes):
            cur = nodes[i]
            i += 1
            for neighbor in cur.neighbors:
                if neighbor not in nodes_map: # 还没有处理过
                    nodes_map[neighbor] = UndirectedGraphNode(neighbor.label)
                    nodes.append(neighbor)

        for n in nodes:
            new_node = nodes_map[n]
            for neighbor in n.neighbors:
                new_node.neighbors.append(nodes_map[neighbor])
        
        return nodes_map[node]
                        
                
        