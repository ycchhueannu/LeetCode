class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # note that in the cases "[-1,-1,-1,0,1,1]",
        # the answer is 0
        if len(nums) <= 2:
            return -1
        s = sum(nums)
        left_s = 0
        for i in range(len(nums)):
            if 2*left_s == s - nums[i]:
                return i
            left_s += nums[i]
        return -1