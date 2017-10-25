# -*- coding: utf-8 -*-

# http://lintcode.com/en/problem/permutations/#

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        
        def helper(current=[]):
            if len(current) == len(nums):
                r.append(current)
                return
            
            for i in range(len(nums)):
                if nums[i] in used:
                    continue

                used.add(nums[i])
                helper(current + [nums[i]])
                used.remove(nums[i])

        r = []
        used = set()
        helper([])
        return r