class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        S = S.replace("abc", "")
        while "abc" in S: # "aaabcbcbc" is true
            S = S.replace("abc", "")
        return not S