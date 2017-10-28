# -*- coding: utf-8 -*-

# 这是个超时的答案
# 听 graph 的最后一部分

from collections import defaultdict
import Queue

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        
        def diff(w1, w2):
            c = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    c += 1
                    
            return c
        
        word_dict = defaultdict(list)
        dict.add(start)
        dict.add(end)
        
        for i, w1 in enumerate(dict):
            for j, w2 in enumerate(dict):
                if i != j and diff(w1, w2) == 1:
                    word_dict[w1].append(w2)
                    word_dict[w2].append(w1)
            
        visited = set()

        queue = Queue.Queue()
        queue.put(start)

        step = 0
        
        while not queue.empty():
            for i in range(queue.qsize()):
                word = queue.get()

                if word in visited:
                    continue
                if word == end:
                    return step + 1

                visited.add(word)
                next_words = word_dict.get(word) or []
                for w in next_words:
                    queue.put(w)
            step += 1

        return -1
            
            
