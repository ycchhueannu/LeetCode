class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ra, ia = a.split('+')
        rb, ib = b.split('+')
        ra, ia = int(ra), int(ia[:-1])
        rb, ib = int(rb), int(ib[:-1])
        return str((ra*rb-ia*ib)) + '+' + str(ra*ib+ia*rb) + 'i'