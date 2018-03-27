from itertools import zip_longest
from functools import reduce
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == "":
            return ""
        if (numRows in [1, len(s)]) or (len(s) < numRows): 
            return s
        
        ans = []
        hop = (numRows - 1) * 2 # hop size
        for i in range(0, numRows):
            if 0 < i < (numRows-1):
                str1 = s[i::hop]
                str2 = s[hop-i::hop]
                ans.append(self.intermixString(str1, str2))
            else:
                ans.append(s[i::hop])
                
        return ''.join(ans)

    def intermixString(self, str1, str2):
        tmpList = list(zip_longest(str1, str2, fillvalue=''))
        return ''.join(reduce(lambda x, y: x+y, tmpList))