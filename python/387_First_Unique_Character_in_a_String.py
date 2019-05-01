class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # only contain lowercase letters
        # return min([s.index(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])
        d = {}
        for idx, key in enumerate(list(s)):
            if key not in d:
                d[key] = idx
            else:
                d[key] = -1
        candidate = filter(lambda x: x != -1, list(d.values()))
        if not candidate:
            return -1
        else:
            return min(candidate)