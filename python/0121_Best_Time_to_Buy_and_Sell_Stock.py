class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        diff_price = []
        for i in range(1, len(prices)):
            diff_price.append(prices[i]-prices[i-1])
            
        ret = 0
        cur_sum = 0
        for diff in diff_price:
            cur_sum += diff
            if cur_sum > 0:
                ret = max(ret, cur_sum)
            else:
                cur_sum = 0
        return ret