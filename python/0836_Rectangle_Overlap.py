class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        a, b, c, d = rec1
        m, n, p, q = rec2
        # draw picture (fix a~d, discuss every possibilities)
        if p > a and q > b:
            if p <= c and q <= d:
                return True
            if p > c and (m < c and n < d):
                return True
            if (p < c and q > d) and (m < c and n < d):
                return True
        
        return False