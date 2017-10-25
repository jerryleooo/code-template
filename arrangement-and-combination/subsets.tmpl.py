# -*- coding: utf-8 -*-

# http://lintcode.com/en/problem/subsets/

class Solution:
    
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        
        r = []
        
        def subsets_helper(path, pos):
            r.append(path)
            
            for i in range(pos, len(nums)):
                subsets_helper(path + [nums[i]], i + 1)
                
        subsets_helper([], 0)
                
        return r