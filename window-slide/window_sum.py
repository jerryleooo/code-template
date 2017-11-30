class Solution:
    """
    @param: nums: a list of integers.
    @param: k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        
        if not nums or not k:
            return []
        
        if len(nums) <= k:
            return [sum(nums), ]
            
        orig = sum(nums[:k-1])
        r = []

        for i, n in enumerate(nums):
            if i + k - 1 >= len(nums):
                break

            orig += nums[i + k - 1]
            r.append(orig)
            orig -= nums[i]
        
        return r
            
            