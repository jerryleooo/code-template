# -*- coding: utf-8 -*-

# Bottom up

class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        
        if not triangle or not triangle[0]:
            return -1
            
        n = len(triangle)
        dp = [[0] * n for i in range(n)]
        
        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
            
        for i in range(n-2, -1, -1):
            for j in range(0, i + 1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
                
        return dp[0][0]

# Top Down
 
class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        
        if not triangle or not triangle[0]:
            return -1
            
        n = len(triangle)
        dp = [[0] * n for i in range(n)]
        
        dp[0][0] = triangle[0][0]
        
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
            
        for i in range(1, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i - 1][j - 1]) + triangle[i][j]

        return min(dp[n - 1])