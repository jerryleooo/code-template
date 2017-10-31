from collections import defaultdict
import Queue

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        
        edges = defaultdict(list)
        degree = defaultdict(int)
        
        for pre, course in prerequisites:
            degree[pre] += 1
            edges[course].append(pre)
            
        queue = Queue.Queue()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.put(i)
                
        count = 0
        while not queue.empty():
            course = queue.get()
            count += 1
            for post in edges[course]:
                degree[post] -= 1
                if degree[post] == 0:
                    queue.put(post)
                    
        return count == numCourses 
        # 充分利用了 bfs 时间复杂度是 N 的特点
        # count 代表最终 result 的一个顺序，有环的话，环里面的元素不会加到 result 里面，从而 count < numCourses