# -*- coding: utf-8 -*-

# http://lintcode.com/en/problem/search-for-a-range/#

class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
        
        start, end = 0, len(A) - 1
        bound = [-1, -1]
        
        # search for the left bound
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                end = mid # 两次二分查找的不同点在这
            elif A[mid] < target:
                start = mid
            else:
                end = mid
                
        if A[start] == target:
            bound[0] = start
        elif A[end] == target:
            bound[0] = end
        else:
            bound[0] = bound[1] = -1
            return bound
        
        # search for the right bound
        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                start = mid # 一个是找左边界，一个是找右边界
            elif A[mid] < target:
                start = mid
            else:
                end = mid
                
        if A[end] == target:
            bound[1] = end
        elif A[start] == target:
            bound[1] = start
        else:
            bound[0] = bound[1] = -1
            return bound
            
        return bound
            