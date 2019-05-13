class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        sqrtc = int(c**0.5)
        for a in range(0, sqrtc+1): # a and b should <= sqrt(c)
            b = (c - a**2)**0.5
            if b == int(b):
                return True
        return False