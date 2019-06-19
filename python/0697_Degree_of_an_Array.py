class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        freq = 1
        n = -1
        d_f = {}
        d_i = {}
        for i in range(len(nums)):
            ni = nums[i]
            if ni not in d_f:
                d_f[ni] = 1
                d_i[ni] = [i]
            else:
                d_f[ni] += 1
                d_i[ni].append(i)
                if d_f[ni] > freq:
                    freq = d_f[ni]
                    n = ni
                elif d_f[ni] == freq and (d_i[ni][-1]-d_i[ni][0] < d_i[n][-1]-d_i[n][0]):
                        n = ni
        if freq == 1:
            return 1
        return d_i[n][-1]-d_i[n][0]+1