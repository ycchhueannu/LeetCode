class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 1]
        for i in range(3, n+1):
            cur = 0
            for x in range(1, i//2 + 1):
                y = i - x
                cur = max(cur, x*y, dp[x]*y, x*dp[y], dp[x]*dp[y])
            dp.append(cur)
        return dp[n]