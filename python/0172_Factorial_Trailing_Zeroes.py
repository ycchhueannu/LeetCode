class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            n_next = n // 5
            cnt += n_next
            n = n_next
        return cnt
        
        """
        since 2 * 5 = 10, and we have enough 2, only need 
        to count how many 5's in n!
        e.g. 75! -> we only need to count 75, 70, 65, ...
        75 = 5*15, 70 = 5*14, ... 5 = 5*1 -> there are 15's
        5. However, we also need to count how many 5's are 
        in 15~1 (multiplier) -> there are 3 5s (15 = 5*3)
        """