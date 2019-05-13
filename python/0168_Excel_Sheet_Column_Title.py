class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # ord("A") = 65 <-> chr(65) = "A"
        if n <= 26:
            return chr(n+64)
        if n%26 == 0: # deal with cases like 52
            return self.convertToTitle(n//26 - 1) + self.convertToTitle(26) # 'Z'
        return self.convertToTitle(n//26) + self.convertToTitle(n%26)