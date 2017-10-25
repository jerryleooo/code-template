# -*- coding: utf-8 -*-

# http://lintcode.com/en/problem/search-insert-position/

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        
        if not A:
            return 0
        
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid # 因为是 no duplicates 数组
            elif A[mid] > target:
                end = mid
            else:
                start = mid
                
        if A[start] >= target:
            return start
        elif A[end] >= target:
            return end
        else:
            return end + 1 # return len(A) 也可以
