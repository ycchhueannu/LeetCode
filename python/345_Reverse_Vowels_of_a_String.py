class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = set(list('aeiouAEIOU'))
        vow_chr = []
        vow_idx = []
        for i, c in enumerate(s):
            if c in vow:
                vow_chr.append(c)
                vow_idx.append(i)
                
        vow_chr.reverse()
        s = list(s)
        for i, c in zip(vow_idx, vow_chr):
            s[i] = c
        
        return ''.join(s)