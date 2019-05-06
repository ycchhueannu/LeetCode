class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        from itertools import izip_longest # zip_longest in python 3
        carry = 0
        rev_ans = ""
        for n1, n2 in izip_longest(num1[::-1], num2[::-1], fillvalue=0):
            num = int(n1) + int(n2) + carry
            carry, digit = num//10, num%10
            rev_ans += str(digit)
        if carry == 1:
            rev_ans += "1"
        return rev_ans[::-1]