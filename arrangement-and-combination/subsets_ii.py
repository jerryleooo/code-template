# -*- coding: utf-8 -*-

# http://lintcode.com/en/problem/subsets-ii/#

class Solution:
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        
        r = []
        
        def subsets_helper(path, pos):
            r.append(path)
            
            for i in range(pos, len(nums)):
                if i > 0 and i != pos and nums[i] == nums[i-1]: # 被跳过了？
                    continue

                subsets_helper(path + [nums[i]], i + 1)
        
        nums.sort()
        subsets_helper([], 0)
        return r