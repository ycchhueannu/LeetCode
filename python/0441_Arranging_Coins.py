class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_layer = int((n*2)**0.5)
        if (max_layer)*(max_layer+1)/2 > n:
            return max_layer-1
        return max_layer