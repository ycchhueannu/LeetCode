class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumulative_sum = [0]
        for i in nums:
            self.cumulative_sum.append(self.cumulative_sum[-1]+i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cumulative_sum[j+1]-self.cumulative_sum[i]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)