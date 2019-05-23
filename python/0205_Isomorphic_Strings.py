class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # similar to 890. Find and Replace Pattern ?
        d_st = {}
        d_ts = {}
        for i in range(len(s)):
            if s[i] not in d_st:
                if t[i] in d_ts and d_ts[t[i]] != s[i]:
                    return False
                d_st[s[i]] = t[i]
                d_ts[t[i]] = s[i]
            elif d_st[s[i]] != t[i]:
                return False
        return True