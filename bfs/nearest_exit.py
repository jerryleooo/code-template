# -*- coding: utf-8 -*-

import Queue

class Solution:
    """
    @param: rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here

        if not rooms:
            return
        
        m = len(rooms)
        n = len(rooms[0])

        queue = Queue.Queue()

        for i, line in enumerate(rooms):
            for j, item in enumerate(line):
                if item == 0:
                    queue.put((i, j))

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = set()
        step = 0
        
        while not queue.empty():
            for i in range(queue.qsize()):
                node = queue.get()
                x, y = node
                rooms[x][y] = min(rooms[x][y], step)

                if node in visited:
                    continue
                
                visited.add(node)
                for dx, dy in directions:
                    if 0 <= x + dx < m and 0 <= y + dy < n and rooms[x+dx][y+dy] != -1:
                        queue.put((x+dx, y+dy))
            step += 1