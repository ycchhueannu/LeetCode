class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join(list(map(lambda x: chr(ord(x)+32) if x.isupper() is True else x, str)))