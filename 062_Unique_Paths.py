from functools import reduce
from operator import mul
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return reduce(mul, range(m, m+n-1)) // reduce(mul, range(1, n)) if 1 not in (m, n) else 1