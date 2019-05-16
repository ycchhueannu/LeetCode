class Solution(object):
    """
    def getPrime(self, num):
        if num == 1:
            return []
        elif num in [2, 3]:
            return [num]
        ub = int(num**0.5)
        num_p = []
        found = False
        for p in range(2, ub+1):
            if num % p == 0:
                found = True
                num_p = [p] + self.getPrime(num//p)
                break
            if p == ub and not found:
                num_p.append(num)
        return num_p
    """    
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        combination = [2, 3, 5, 6, 10, 15, 30]
        while num > 1:
            found = False
            for c in combination:
                if num % c == 0:
                    found = True
                    num //= c
                    break
            if not found:
                return False
        return True
        
        """
        if num <= 0:
            return False
        ub = int(num**0.5)
        num_p = self.getPrime(num)
        #print(num_p)
        if any(i > 5 for i in num_p):
            return False
        else:
            return True
        """