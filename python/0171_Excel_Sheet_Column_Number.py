class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ord('A') = 65
        num = 0
        cnt = 0
        for c in s[::-1]:
            num += (ord(c)-64)* 26**cnt
            cnt += 1
        return num