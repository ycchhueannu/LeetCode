class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        # iterate from N to 1 is a lot faster than from 1 to N
        # range() will introduce memory error when N is large
        # in python 2, should use xrange() instead (python 3
        # does not face this problem tho)
        for i in xrange(N, 0, -1):
            if format(i, "b") not in S:
                return False
        return True