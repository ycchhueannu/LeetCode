class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = {i: 0 for i in map(chr, range(97, 123))}
        for i in s:
            d[i] += 1
        for i in t:
            d[i] -= 1
        for i in d:
            if d[i] != 0:
                return False
        return True