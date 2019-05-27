class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d_ps = {}
        d_sp = {}
        s = str.split(' ')
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d_ps:
                if s[i] in d_sp and d_sp[s[i]] != pattern[i]:
                    return False
                d_ps[pattern[i]] = s[i]
                d_sp[s[i]] = pattern[i]
            elif d_ps[pattern[i]] != s[i]:
                return False
        return True