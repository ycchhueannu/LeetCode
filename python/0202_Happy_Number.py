class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set()
        while True:
            if n == 1:
                return True
            elif n in d:
                return False
            d.add(n)
            n = sum([int(i)**2 for i in str(n)])