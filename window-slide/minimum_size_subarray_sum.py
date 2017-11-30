class Solution:
    """
    @param: nums: an array of integers
    @param: s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        j = i = 0
        sum = 0
        ans = float('inf')
        
        for i in range(len(nums)):
            while j < len(nums) and sum < s:
                sum += nums[j]
                j += 1
            
            if sum >= s:
                ans = min(ans, j - i)
                
            sum -= nums[i]
            
        if ans == float('inf'):
            ans = -1
            
        return ans