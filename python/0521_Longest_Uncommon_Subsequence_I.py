class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) == len(b) and a in b:
            return -1
        return max(len(a), len(b))