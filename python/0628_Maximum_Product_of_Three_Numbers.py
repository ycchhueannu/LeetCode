class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max1 = nums[-1]*nums[-2]*nums[-3]
        max2 = nums[-1]*nums[0]*nums[1]
        # +++ or +--
        return max(max1, max2)