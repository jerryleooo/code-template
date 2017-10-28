class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        
        def get_is_palindrome(s):
            
            is_palindrome = [[False] * len(s) for i in range(len(s))]
            
            for i in range(len(s)):
                is_palindrome[i][i] = True
                
            for i in range(len(s) - 1):
                is_palindrome[i][i+1] = s[i] == s[i+1]
                
            for length in range(2, len(s)):
                start = 0
                while start + length < len(s):
                    is_palindrome[start][start + length] = is_palindrome[start + 1][start + length - 1] and s[start] == s[start + length]
                    start += 1
                    
            return is_palindrome
            
        if not s:
            return 0
            
        is_palindrome = get_is_palindrome(s)
        dp = [0] * (len(s) + 1)
        
        for i in range(1, len(s) + 1):
            dp[i] = float('inf')
            for j in range(i):
                if is_palindrome[j][i-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
                    
        return dp[-1]