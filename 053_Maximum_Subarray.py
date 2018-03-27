class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums == []:
            return None
        
            
        
        gb_max = nums[0]
        cur_sum = 0
        
        for i in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += i
            if cur_sum > gb_max: # note that max() is much slower than this if-statement
                gb_max = cur_sum
        
        return gb_max