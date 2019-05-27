class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        num = sorted(d.keys())
        ret = 0
        for i in range(0, len(num)-1):
            if num[i+1] - num[i] == 1:
                ret = max(ret, d[num[i+1]]+d[num[i]])
        return ret