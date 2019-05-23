class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {i: 0 for i in map(chr, range(97, 123))}
        for i in t:
            d[i] += 1
        for i in s:
            d[i] -= 1
        for i in d:
            if d[i]:
                return i
        #return chr(sum([ord(i) for i in t]) - sum([ord(i) for i in s]))