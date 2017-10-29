from collections import defaultdict
import Queue
import string

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
                    if next in dict:
                        r.append(next)
            return r

        dict.add(start)
        dict.add(end)
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
                for w in get_next_word(word):
                    queue.put(w)
            step += 1

        return -1
            
            
