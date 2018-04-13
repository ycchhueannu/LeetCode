class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        d = {0: 0, 1: 0, 2: 0}
        for i in nums:
            d[i] += 1
        nums[:] = [0] * d[0] + [1] * d[1] + [2] * d[2]