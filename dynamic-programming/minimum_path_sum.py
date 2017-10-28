class Solution:
    """
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        
        if not grid or not grid[0]:
            return 0
        
        M = len(grid)
        N = len(grid[0])
        sum = [[0] * N for i in range(M)]
        
        sum[0][0] = grid[0][0]
        
        for i in range(1, M):
            sum[i][0] = sum[i-1][0] + grid[i][0]
            
        for i in range(1, N):
            sum[0][i] = sum[0][i-1] + grid[0][i]
            
        for i in range(1, M):
            for j in range(1, N):
                sum[i][j] = min(sum[i-1][j], sum[i][j-1]) + grid[i][j]
                
        return sum[M-1][N-1]