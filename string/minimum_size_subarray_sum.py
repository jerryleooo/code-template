class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        min_length = 1 << 31
    
        if not nums:
            return 0
    
        left, right = 0, 0
        cur = nums[left]
        
        if cur >= s and right - left + 1 < min_length:
            min_length = right - left + 1
        
        while right < len(nums) and left <= right:
            # print left, right, cur
            if cur >= s:
                cur -= nums[left]
                left += 1

            else:
                right += 1
                if right >= len(nums):
                    break
                        
                cur += nums[right]
                
            if cur >= s and right - left + 1 < min_length:
                min_length = right - left + 1
                
        return 0 if min_length == 1 << 31 else min_length
