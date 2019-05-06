class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        rev_ret = ""
        i = len(a) - 1
        j = len(b) - 1
        c = 0 # carry
        while i >= 0 and j >= 0:
            cur_val = int(a[i]) + int(b[j]) + c
            c, v = cur_val // 2, cur_val % 2
            rev_ret += str(v)
            i -= 1
            j -= 1
        while i >= 0:
            cur_val = int(a[i]) + c
            c, v = cur_val // 2, cur_val % 2
            rev_ret += str(v)
            i -= 1
        while j >= 0:
            cur_val = int(b[j]) + c
            c, v = cur_val // 2, cur_val % 2
            rev_ret += str(v)
            j -= 1
        if c == 1:
            rev_ret += str(c)
        
        return rev_ret[::-1]