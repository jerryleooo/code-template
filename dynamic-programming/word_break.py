# -*- coding: utf-8 -*-

# Accept answer

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        
        if not s:
            return True
            
        if not dict:
            return False

        max_length = 0

        for word in dict:
            max_length = max(max_length, len(word))

        dp = [False] * (len(s) + 1)
        dp[0] = [True]
        
        for i in range(1, len(s) + 1):
            j = i - 1
            while j >= 0 and i - j <= max_length:
                if s[j:i] in dict and dp[j]:
                    dp[i] = True
                    break
                j -= 1
        
        return dp[-1]

# BFS Answer, 会超时
from collections import defaultdict
import Queue

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        
        if not dict:
            if not s:
                return True
            return False
        
        max_length = 0
        min_length = float('inf')
        for word in dict:
            max_length = max(max_length, len(word))
            min_length = min(min_length, len(word))
        
        edges = defaultdict(list)
        for i in range(min_length, len(s) + 1):
            j = max(0, i - max_length)
            while j < i:
                if s[j:i] in dict:
                    edges[i].append(j)
                j += 1

        queue = Queue.Queue()
        queue.put(len(s))
        
        while not queue.empty():
            node = queue.get()
            if node == 0:
                return True

            for n in edges[node]:
                queue.put(n)
                
        return False