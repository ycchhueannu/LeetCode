class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = [i for i in s.lower() if i.isalnum()]
        return tmp == tmp[::-1]