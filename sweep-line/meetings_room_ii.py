# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        if not intervals:
            return 0
        
        timepoints = []
        for interval in intervals:
            timepoints.append((interval.start, 1))
            timepoints.append((interval.end, -1))
            
        timepoints.sort()
        
        s, most = 0, 0
        for k, delta in timepoints:
            s += delta
            most = max(most, s)
            
        return most