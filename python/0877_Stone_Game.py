class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        s =[0]
        for p in piles:
            s.append(s[-1]+p)
        
        for i in range(n):
            dp[i][i] = piles[i]
        
        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i + l - 1
                dp[i][j] = max(dp[i][i] + (s[j+1]-s[i+1]-dp[i+1][j]),
                              dp[j][j] + (s[j]-s[i]-dp[i][j-1]))

        return dp[0][n-1] > s[-1]/2

        """
        Let A[i..j] be the optimal stones that Alex can get from piles[i..j] 
        (include i and j), we can easily know that the answer should be A[0..n-1].

        DP formula: A[i..j] = max(A[i..i][1st]+A[i+1..j][2nd], A[j..j][1st]+A[i..j-1][2nd])
        Note that "1st" means first one to pick, and "2nd" means the second one to pick.

        To save spaces (no need to store another n*n array), I re-write and get 2nd 
        person's number of stones. (it may be slower)

        Note also that A[x][y][1st] is not always larger than A[x][y][2nd]". For example, 
        in the [5, 100, 200, 7] cases, if we look at subarray [100, 200, 7], the first
        person to choose will always get 100+7, while the second one will get 200.

        example:
        piles = [5, 100, 200, 7]
        s = [0, 5, 105, 305, 312]

        A =   5 100 205 205
              0 100 200 107
              0   0 200 200
              0   0   0   7
        """