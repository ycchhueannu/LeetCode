class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = [None] * len(nums)
        for i in nums:
            if i > 0:
                try:
                    tmp[i-1] = 1
                except:
                    continue
        try:
            ans = tmp.index(None) + 1
            return ans
        except:
            return len(tmp) + 1