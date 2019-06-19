class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) in [0, 1]:
            return len(nums)
        start = 0
        ret = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                pass
            else:
                ret = max(ret, i-start)
                start = i
        ret = max(ret, i-start+1)
        return ret