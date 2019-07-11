class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n_row = len(matrix)
        n_col = len(matrix[0])
        dp = [[0 for _ in range(n_col)] for _ in range(n_row)]
        ret = 0
        for j in range(n_col):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                ret = 1
        for i in range(n_row):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                ret = 1
        for i in range(1, n_row):
            for j in range(1, n_col):
                if matrix[i][j] == "1" and dp[i-1][j-1] >= 1 and dp[i-1][j] >= 1 and dp[i][j-1] >= 1:
                    min_num = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    dp[i][j] = min_num + 1 
                    if dp[i][j] > ret:
                        ret = dp[i][j]
                else:
                    dp[i][j] = int(matrix[i][j])
        return int(ret**2)