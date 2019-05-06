class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for n in range(1, len(s)//2 + 1):
            if len(s) % n == 0:
                sub_str = s[0:n]
                if all(s[n*i:n*(i+1)] == sub_str for i in range(0, len(s)//n)):
                    return True
        return False