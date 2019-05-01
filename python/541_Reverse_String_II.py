class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ret = ""
        i = 0
        while i < len(s):
            ret += s[i:i+k][::-1] + s[i+k:i+2*k]
            i += 2*k
        return ret