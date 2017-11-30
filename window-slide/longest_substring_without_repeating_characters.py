class Solution:
    """
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        
        visit = [0] * 256
        ans = 0
        j = 0

        for i in range(len(s)):
            while j < len(s) and visit[ord(s[j])] == 0:
                visit[ord(s[j])] = 1
                ans = max(ans, j - i + 1)
                j += 1
                
            visit[ord(s[i])] = 0
        return ans


# Second Method
# 其实自己也想到了，还是没有自信
 
class Solution:
    """
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        
        visit = set()
        ans = 0
        j = 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in visit:
                visit.add(s[j])
                ans = max(ans, j - i + 1)
                j += 1
                
            visit.remove(s[i])
        return ans