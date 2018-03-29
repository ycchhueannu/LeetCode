class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        d = {0:[0], 1: [0, 1], 2: [0, 1, 3, 2]}
        
        if n in [1, 2]:
            return d[n]
        
        for i in range(2, n):
            #d[i+1] = d[i] + list(map(lambda x: x + (1 << i), d[i][::-1]))
            d[i+1] = d[i] + [2**(i) + x for x in (d[i])[::-1]]
        
        return d[n]