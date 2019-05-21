class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = {}
        for i in A:
            if i not in d:
                d[i] = 1
            else:
                return i