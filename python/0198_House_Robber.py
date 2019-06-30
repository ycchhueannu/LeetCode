class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        dp = [0, nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1]+nums[i], dp[i]))
        return dp[-1]
        """
        it can be formulated as:
                         { nums[0..i-2] + a[i]
        nums[0..i] = max {
                         { nums[0..i-1]
        """