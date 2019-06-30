class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0]
        pre_pow2 = 1
        for i in range(1, num+1):
            if not (i & (i-1)): # is power of 2
                ret.append(1)
                pre_pow2 = i
            else:
                ret.append(1 + ret[i-pre_pow2])
        return ret
        """
        Note:
        we know that the power of two numbers represented as binary
        have only 1 bit-1 (e.g. 4 = 100, 16 = 1000). And for numbers
        in [2**(n), 2**(n+1)), this bit-1 will never be changed.
        so for the number (say, p) in this interval, we can count it as
        1 + (# bit-1 in p-2**n). For example, 7 = 4 + 3, and the binary
        representation is 100 + 011, which is 1 + (# bit-1 in 3) = 1+2
        """