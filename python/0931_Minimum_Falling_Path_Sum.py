class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        dp = [[] for i in range(n)]
        for i in A[0]:
            dp[0].append(i)
        for i in range(1, n):
            for j in range(0, n):
                dp[i].append(min(dp[i-1][j and j-1: j+2]) + A[i][j])

        return min(dp[n-1])
        """
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + A[i][j]

        note that in line 13, I normally would write these lines:
                if j == 0:
                    dp[i].append(min(dp[i-1][j], dp[i-1][j+1]) + A[i][j])
                elif j == n-1:
                    dp[i].append(min(dp[i-1][j-1], dp[i-1][j]) + A[i][j])
                else:
                    dp[i].append(min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + A[i][j])
        """