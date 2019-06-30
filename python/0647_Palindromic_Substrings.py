class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cnt = n
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        # length = 2 case
        for i in range(0, n-1):
            j = i + 1
            if s[i] == s[j]:
                dp[i][j] = 1
                cnt += 1
            else:
                dp[i][j] = 0
        
        for l in range(3, n+1):
            for i in range(0, n-l+1):
                j = i + l - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = 1
                    cnt += 1
                else:
                    dp[i][j] = 0
        #print(dp)
        return cnt
        """
        if s[i..j] is a palindromic substring, then
        s[i+1..j-1] is also a palindromic substring.
                   { 1, if s[i] == s[j] and dp[i+1][j-1] == 1
        dp[i][j] = {
                   { 0, otherwise
        For example, s = "aba"
        dp = 
             a b a
           a 1 x z
           b   1 y
           a     1
        To compute z (dp[0][2]), we test if s[0] == s[2] and 
        dp[1][1] == 1. Since dp[1][1] means substring "b", it's
        a palindromic substring, and s[0] == a == s[2], z = 1.  

        note that for the length = 2 cases, like x and y in the dp
        array, we can't access elements in the left-bottom part.

        """