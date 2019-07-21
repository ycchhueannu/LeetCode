class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(s):
            while j < len(t):
                if s[i] != t[j]:
                    j += 1
                else:
                    i += 1
                    j += 1
                    break
            if j == len(t):
                break
        return i == len(s)