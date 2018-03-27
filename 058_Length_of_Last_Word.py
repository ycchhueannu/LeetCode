class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        l = list(filter(lambda x: x is not '', s.split(' ')))
        if l == []:
            return 0
        return len(l[-1])