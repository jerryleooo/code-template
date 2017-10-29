# -*- coding: utf-8 -*-

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        
        def helper(current):
            if len(current) == len(nums):
                result.append(current)
                return
            
            for i, n in enumerate(nums):
                if i in used or \
                   i > 0 and i - 1 in used and nums[i] == nums[i-1]:
                       continue
                   
                used.add(i)
                helper(current + [n])
                used.remove(i)
        
        nums.sort()
        result = []
        used = set()
        helper([])
        return result