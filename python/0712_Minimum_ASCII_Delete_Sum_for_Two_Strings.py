class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(0, len(s2)):
            dp[0][i+1] = dp[0][i] + ord(s2[i])
        for i in range(0, len(s1)):
            dp[i+1][0] = dp[i][0] + ord(s1[i])
        
        for i in range(len(s1)):
            for j in range(len(s2)):
                cur_i, cur_j = i+1, j+1
                if s1[i] == s2[j]:
                    dp[cur_i][cur_j] = dp[cur_i-1][cur_j-1]
                else:
                    dp[cur_i][cur_j] = min(dp[cur_i-1][cur_j]+ord(s1[i]), dp[cur_i][cur_j-1]+ord(s2[j]))
        return dp[-1][-1]