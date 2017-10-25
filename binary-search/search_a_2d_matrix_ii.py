# -*- coding: utf-8 -*-

# http://lintcode.com/en/problem/search-a-2d-matrix-ii/

class Solution:
    """
    @param: matrix: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here

        if not matrix or not matrix[0]:
            return 0
            
        n = len(matrix)
        m = len(matrix[0])
        x = n - 1
        y = 0
        count = 0
        
        while x >= 0 and y < m:
            if matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                count += 1
                x -= 1
                y += 1
                
        return count
