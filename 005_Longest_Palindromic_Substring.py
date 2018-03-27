class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: # empty string
            return ""
        if s == s[::-1]: # LPS of s its itself
            return s
        
        # l is (n+1)*(n+1) matrix, stands for 'length'
        
        # there are 94 test cases
        #l = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        l = [ _[:] for _ in [[0] * (len(s)+1)] * (len(s)+1)] # optimize
        
        """
        if s = "zzzcdabdczzz", then we need to know that after reverse string s, i.e. p = "zzzcdbadczzz"
        'zzzcd' can't be the LPS of s
        """
        #idxAlign = lambda i, j: ((len(s)-i+1) == (j-l[i][j]+1)) and ((len(s)-(i-l[i][j]+1)+1) == j)
        """arange equality test, observe that the latter is the same as the former one"""
        idxAlign = lambda i, j: (len(s) + l[i][j]) == (i + j)
        
        # do LCS of s and p (reverse of s)        
        # index is 1..len(s), NOT starts from 0
        p = s[::-1] # p is string s 'in reverse'
        max_len = 1 # length of longest palindromic substring, minimum is 1 (empty string is dealt with from above)
        end_i, end_j = 1, 1 # record index, note that end_i records end of string s, end_j record string p
        
        for i in range(1, len(s)+1):
            for j in range(1, len(s)+1):
                
                if (s[i-1] == p[j-1]):
                    l[i][j] = l[i-1][j-1] + 1
                    if (l[i][j] > max_len) and idxAlign(i, j): # update
                        (max_len, end_i, end_j) = (l[i][j], i, j)
                else: # s[i-1] != p[j-1]
                    l[i][j] = 0
                    
        # end for
        
        if max_len == 1:
            return s[0] # return whichever character in s
        
        #print("length of s:", len(s), "max_len:", max_len)
        #print("end_i:", end_i, ", end_j: ", end_j)
        #start = len(s) - end_j
        #end = end_i
        #print("start:{}, end:{}".format(start, end))
        return s[len(s)-end_j : end_i] # return index 'start' ~ 'end - 1'