class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in strs:
            grp_key = ''.join(sorted(i))
            if grp_key not in d:
                d[grp_key] = [i]
            else:
                d[grp_key] += [i]
        return list(d.values())