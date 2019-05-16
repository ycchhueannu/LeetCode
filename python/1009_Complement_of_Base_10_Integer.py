class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        return int(''.join(map(lambda x: '1' if x == '0' else '0', s)), 2)