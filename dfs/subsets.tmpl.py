class Solution:
    
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        
        def helper(current, start):
            result.append(current)
            
            for i in range(start, len(nums)):
                helper(current + [nums[i]], i + 1)
        
        nums.sort()
        result = []
        helper([], 0)
        return result