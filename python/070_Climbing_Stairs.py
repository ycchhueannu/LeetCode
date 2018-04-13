class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        An_2 = 1; An_1 = 1
        ans = 1
        for i in range(1, n):
            ans = An_2 + An_1
            An_2 = An_1
            An_1 = ans
        return ans