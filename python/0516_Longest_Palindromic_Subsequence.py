class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)]
        s_rev = s[::-1]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s_rev[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]