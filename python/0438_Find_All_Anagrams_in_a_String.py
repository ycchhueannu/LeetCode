class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        elif len(p) == len(s):
            d_p = {i: p.count(i) for i in set(p)}
            d_s = {i: p.count(i) for i in set(s)}
            if d_p == d_s:
                return [0]
            else:
                return []
        else:
            ret = []
            d_p = {}
            for i in p:
                if i not in d_p:
                    d_p[i] = 1
                else:
                    d_p[i] += 1
            cur = {}
            for i in s[0:len(p)]:
                if i not in cur:
                    cur[i] = 1
                else:
                    cur[i] += 1
            
            start = 0
            end = len(p)-1
            while end < len(s):
                if cur == d_p:
                    ret.append(start)
                cur[s[start]] -= 1
                if cur[s[start]] == 0:
                    del cur[s[start]]
                start += 1
                
                end += 1
                if end == len(s):
                    break
                if s[end] not in cur:
                    cur[s[end]] = 1
                else:
                    cur[s[end]] += 1
            return ret
                