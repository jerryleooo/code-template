class Solution:
    """
    @param: A: An integer array
    @param: k: A positive integer (k <= length(A))
    @param: target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        n = len(A)
        dp = [[[0] * (target + 1) for i in range(k + 1)] for j in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0][0] = 1
            
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for t in range(1, target + 1):
                    dp[i][j][t] = 0
                    if t >= A[i - 1]:
                        dp[i][j][t] = dp[i - 1][j - 1][t - A[i - 1]]
                    dp[i][j][t] += dp[i - 1][j][t]
                    
        return dp[n][k][target]