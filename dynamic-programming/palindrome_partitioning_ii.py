class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        
        def get_is_palindrome(s):
            matrix = [[False] * n for i in range(n)]

            for i in range(n):
                matrix[i][i] = True

            for i in range(n-1):
                matrix[i][i+1] = s[i] == s[i+1]
            
            for i in range(n-3, -1, -1):
                for j in range(i+2, n):
                    matrix[i][j] = matrix[i+1][j-1] and s[i] == s[j]
                    
            return matrix
            
        '''
        dp, is_palindrome, s 的对应关系是本题的关键，也是比较容易混乱的地方
        看 palindrome partitioning 的代码能看出期中的关系   
        '''
            
        n = len(s)
        is_palindrome = get_is_palindrome(s)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = i
            for j in range(i):
                if is_palindrome[j][i - 1]:
                    dp[i] = min(dp[j] + 1, dp[i])

        return dp[n] - 1 # 不明白这里为何是 -1
        # 最少能分割成的字符串 - 1 = 最少分割次数