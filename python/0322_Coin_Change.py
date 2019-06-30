class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = {c: 1 for c in coins}
        for i in range(1, amount+1):
            if i not in dp:
                dp[i] = amount + 1
                for c in coins:
                    if c < i:
                        dp[i] = min(dp[i], dp[c] + dp[i-c])
        #print(dp)
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]
        
        """
        dp = {c: 1 for c in coins}
        dp[0] = 0
        def top_down_approach(remain):
            if remain in dp:
                return dp[remain]
            
            dp[remain] = amount + 1
            for c in coins:
                if remain > c:
                    dp[remain] = min(dp[remain], dp[c] + top_down_approach(remain-c))
            return dp[remain]
        
        ret = top_down_approach(amount)
        #print(dp)
        if ret > amount:
            return -1
        else:
            return ret
        """