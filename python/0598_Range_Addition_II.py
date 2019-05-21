class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # assume 1 <= a <= m, 1 <= b <= n
        if not ops:
            return m*n
        row, col = zip(*ops)
        return min(row)*min(col)