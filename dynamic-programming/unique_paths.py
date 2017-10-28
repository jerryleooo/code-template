class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        r = [[0] * n for i in range(m)]
        
        for i in range(m):
            r[i][0] = 1
            
        for i in range(n):
            r[0][i] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                r[i][j] = r[i][j-1] + r[i-1][j]
                
        return r[m-1][n-1]