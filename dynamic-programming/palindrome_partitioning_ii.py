class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def minCut(self, s):
        # write your code here

        def get_is_palindrome():
            matrix = [[0] * n for i in range(n)]
            
            for i in range(n):
                matrix[i][i] = True
                
            for i in range(n-1):
                matrix[i][i+1] = s[i] == s[i+1]
                
            for i in range(n-3, -1, -1):
                for j in range(i + 2, n):
                    matrix[i][j] = matrix[i+1][j-1] and s[i] == s[j]
                    
            return matrix
            
        if not s:
            return []
            
        n = len(s)
        is_palindrome = get_is_palindrome()
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = float('inf')
            for j in range(i):
                if is_palindrome[j][i-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
                    
        return dp[-1] - 1