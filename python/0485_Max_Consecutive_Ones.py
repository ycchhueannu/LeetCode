class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = -1
        cnt = 0
        for i in nums:
            if i == 1:
                cnt += 1
            elif cnt:
                ret = max(ret, cnt)
                cnt = 0
        ret = max(ret, cnt)
        return ret