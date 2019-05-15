class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        if len(s) < 1:
            return 0
        i = 0
        j = 1
        cur_max = 0
        while j < len(s):
            if s[j] != '1':
                j += 1
            else:
                if s[i] == '1':
                    cur_max = max(cur_max, j-i)
                    j += 1
                i += 1
        return cur_max