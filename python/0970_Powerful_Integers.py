class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        from math import log
        if x == 1:
            if y == 1:
                return [2] if bound >= 2 else []
            return self.powerfulIntegers(y, x, bound)
        if y == 1:
            s = set()
            for i in range(0, int(log(bound)/log(x))+1):
                n = x**i + 1
                if n > bound:
                    break
                s.add(n)
            return list(s)
        
        s = set()
        for i in range(0, int(log(bound)/log(x))+1):
            for j in range(0, int(log(bound)/log(y))+1):
                xi, yj = x**i, y**j
                if xi > bound or yj > bound:
                    break
                n = xi + yj
                if n <= bound:
                    s.add(n)
        return list(s)