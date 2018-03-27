class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d = {} # initial empty dictionary
        
        for i, elt in enumerate(nums): # element
            if elt in d:
                return[d[elt], i]
            else:
                d[target-elt] = i # record residual