class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] * 366 # days 0 will cost 0 dollar
        dp[days[0]] = min(costs)
        for i in range(1, len(days)):
            prev_travel_day_cost = dp[days[i-1]]
            for di in range(days[i-1]+1, days[i]):
                dp[di] = prev_travel_day_cost
            
            buy_day30_pass = dp[days[i]-30] + costs[2] if days[i] > 30 else costs[2]
            buy_day7_pass = dp[days[i]-7] + costs[1] if days[i] > 7 else costs[1]
            buy_day1_pass = dp[days[i]-1] + costs[0]
            
            dp[days[i]] = min(buy_day30_pass, buy_day7_pass, buy_day1_pass)
        return dp[days[-1]]