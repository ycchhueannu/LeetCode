class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
            n = 10
        ans = [1, 10]
        mult = [1]
        for i in range(1, 10):
            mult.append((10-i)*mult[-1])
            ans.append(ans[-1]+9*mult[-1])
        return ans[n]
        """
        n = 1 case: (# n = 0 cases) + (numbers have 1 digits)
        Thus, it's 1 + 9 = 10
        
        n = 2 case: (# n = 0 cases) + (# n = 1 cases) + (numbers have 2 digits) _ _
        Thus, it's 10 + 9*9 = 91 (tens digit has to be 1~9, and the ones digit 
        can be 0~9 but not the same as tens digit, so it's 10-1 which equals 9)
        
        n = 3 case: (# n = 0~2 cases) + (numbers have 3 digits) _ _ _
        Thus, it's 91 + 9*9*8 (hundreds digits has to be 1~9, ....)
        
        n = k case: ans(k-1) + 9*9*8*7*6*...
        """
        # n = 2, ans = 91 = 10 + 9*9
        # n = 3, ans = 739 = 91 + 9*9*8