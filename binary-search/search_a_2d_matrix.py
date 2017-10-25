# -*- coding: utf-8 -*-

# http://www.lintcode.com/en/problem/search-a-2d-matrix/

# Binary Searce Twice

class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        
        if not matrix or not matrix[0]:
            return False
            
        row = len(matrix)
        col = len(matrix[0])
        
        start = 0
        end = row - 1
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
                
        if matrix[end][0] <= target:
            row = end
        elif matrix[start][0] <= target:
            row = start
        else:
            return False
            
        start, end = 0, col - 1
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid
            else:
                end = mid
                
        if matrix[row][start] == target:
            return True
        elif matrix[row][end] == target:
            return True
        else:
            return False

# Binary Search Once
# 万变不离其中

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
            
        row, col = len(matrix), len(matrix[0])
        
        start, end = 0, row * col - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            number = matrix[mid / col][mid % col]
            
            if number == target:
                return True
            elif number > target:
                end = mid
            else:
                start = mid
                
        if matrix[start / col][start % col] == target or matrix[end / col][end % col] == target:
            return True
                
        return False