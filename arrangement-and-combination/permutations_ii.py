# -*- coding: utf-8 -*-

# http://lintcode.com/en/problem/permutations-ii/#

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        r = []
        
        def helper(current):
            if len(current) == len(nums):
                r.append(current)
                return

            for i, n in enumerate(nums):
                if i in used or \
                   i > 0 and i - 1 in used and nums[i] == nums[i-1]:
                    # 跟 subsets ii 的那个条件好像
                    # 想像成一棵树，如果这个节点一样，那么下面的子树肯定也是一样的
                    continue

                used.add(i)
                helper(current + [n])
                used.remove(i)

        nums.sort()
        used = set()
        helper([])     
        return r
        