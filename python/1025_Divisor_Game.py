class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        rec_win = {0: False, 1: False}
        for n in range(1, N+1): # n <= N
            for x in range(n-1, 0, -1): # 1 <= x <= N-1
                if n % x == 0 and not rec_win[n-x]: # Bob's next move should not win
                    rec_win[n] = True
                    break
            if n not in rec_win:
                rec_win[n] = False
        return rec_win[N]