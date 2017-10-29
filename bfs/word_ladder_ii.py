# -*- coding: utf-8 -*-
# Leetcode Version

import Queue
import string


class Solution(object):
    def findLadders(self, start, end, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def diff(w1, w2):
            c = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    c += 1
                    if c > 1:
                        return False
            return True
            
        def get_next_word(word):
            r = []
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    if c == word[i]:
                        continue
    
                    next = "".join([word[:i], c, word[i+1:]])
                    if next in word_set:
                        r.append(next)
            return r

        def bfs():
            word_set.add(start)
            # word_set.add(end)
            visited = set()
            queue = Queue.Queue()
            queue.put((start, 0))

            while not queue.empty():
                for i in range(queue.qsize()):
                    word, step = queue.get()
    
                    if word in visited:
                        continue
    
                    if word == end:
                        graph[end] = step
                        return step
    
                    visited.add(word)
                    for w in get_next_word(word):
                        graph[w] = graph.get(w, step + 1)
                        queue.put((w, step + 1))
                        
            return -1

        def dfs(start_word, step, current):
            if start_word == start:
                result.append(current[::-1])
                return

            for word in get_next_word(start_word):
                if word in graph and graph[word] == step - 1:
                    dfs(word, step - 1, current + [word])

        word_set = set(wordList)
        graph = {}
        step = bfs()
        if step != -1:
            graph[start] = 0
            # print graph
            result = []
            dfs(end, step, [end])
            return result
        return []
        