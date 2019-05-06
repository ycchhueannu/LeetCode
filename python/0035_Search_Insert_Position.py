class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return len( list(filter(lambda x: x < target, nums)) )
    
        
        """
        if target in nums:
            return nums.index(target)
        else:
            return len( list(filter(lambda x: x < target, nums)) )
        """