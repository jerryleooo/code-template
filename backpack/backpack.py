# -*- coding: utf8 -*-

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        dp = [[False] * (m + 1) for i in range(len(A) + 1)]

        for i in range(1, m + 1):
            dp[0][i] = False
            
        for i in range(0, len(A) + 1):
            dp[i][0] = True
            
        for i in range(1, len(A) + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i-1][j]
                # 如果不放当前元素如何
                if j >= A[i-1] and dp[i-1][j-A[i-1]]:
                    # 由于 i 的范围是 1 到 len(A) + 1，因此这里应该是 i - 1 表示是否放 A 的这个元素
                    dp[i][j] = True
                    
        for i in range(m, -1, -1):
            if dp[len(A)][i]:
                return i
