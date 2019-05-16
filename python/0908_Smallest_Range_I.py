class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = max(A) - min(A) - 2*K
        if n > 0:
            return n
        else:
            return 0