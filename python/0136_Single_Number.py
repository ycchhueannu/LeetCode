class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            ans ^= i
        return ans
        
        #from functools import reduce
        #from operator import xor
        #return reduce(xor, nums)