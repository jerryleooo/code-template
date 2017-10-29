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


# 自己写的版本
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        def helper(current, remains):
            if not remains:
                result.append(current)
                return
            
            for i, n in enumerate(remains):
                helper(current + [n], remains[:i] + remains[i+1:])
        
        result = []
        helper([], nums)
        return result

# 自己写的版本缺点在于出现了数组拼接，而模版中的答案用了 used 来实现更快的排除已在当前结果中的情况