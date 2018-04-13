class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d1 = {} # char(key) -> index(value)
        ans = 0 # for empty string: ""
        
        start = 0
        for cur in range(len(s)): # current index
            if (s[cur] in d1) and (d1[s[cur]] >= start):
                start = d1[s[cur]]+1
            d1[s[cur]] = cur
            if cur - start + 1 > ans:
                ans = cur - start + 1
            
        return ans  