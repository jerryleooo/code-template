class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        def get_is_palindrome():
            matrix = [[False] * n for i in range(n)]
            
            for i in range(n):
                matrix[i][i] = True
                
            for i in range(n-1):
                matrix[i][i+1] = s[i] == s[i+1]
                
            for i in range(n-3, -1, -1):
                for j in range(i + 2, n):
                    matrix[i][j] = matrix[i+1][j-1] and s[i] == s[j]
                    
            return matrix
            
        def helper(start, current):
            if start == n:
                result.append(current)
                return
            
            for i in range(start, n):
                if not is_palindrome[start][i]:
                    continue
                helper(i + 1, current + [s[start:i+1]])
            
        n = len(s)
        is_palindrome = get_is_palindrome()
        result = []
        helper(0, [])
        return result