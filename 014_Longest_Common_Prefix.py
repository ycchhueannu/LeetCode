class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        
        min_len = min([len(s) for s in strs])
        if min_len == 0:
            return ""
        
        ans = []
        for i in range(0, min_len):
            if all(strs[0][i] == s[i] for s in strs):
                ans.append(strs[0][i])
            else:
                break
                
        return ''.join(ans)