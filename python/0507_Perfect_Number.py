class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 2:
            return False
        l = [1]
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                l.append(i)
                l.append(num//i)
        if sum(l) == num:
            return True
        return False