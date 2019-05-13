class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1~9 has 1*9 digits, 10~99 has 2*90 digits,
        # 100~999 has 3*900 digits ...
        i = 1
        j = 9
        while True:
            num = i*j
            if n > num:
                n -= num
                i += 1
                j *= 10
            else:
                break
        start_num = 10**(i-1) + (n//i - 1)
        ith_digit = n - (n//i)*i
        if ith_digit > 0:
            return str(start_num+1)[ith_digit-1]
        else:
            return str(start_num)[-1]