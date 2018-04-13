class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import factorial
        return int(factorial(2*n) / (factorial(n+1) * factorial(n)))