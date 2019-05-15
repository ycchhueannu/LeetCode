class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        sum_set_nums = sum(set(nums))
        dup = sum(nums) - sum_set_nums
        miss = n*(n+1)//2 - sum_set_nums
        return [dup, miss]