class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        d = [0]*60
        cnt = 0
        for t in time:
            d[t%60] += 1
        
        cnt += d[0]*(d[0]-1)//2
        for i in range(1, 30):
            if d[i] and d[60-i]:
                cnt += d[i]*d[60-i]
        cnt += d[30]*(d[30]-1)//2
        
        return cnt