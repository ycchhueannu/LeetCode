class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ret = []
        for word in words:
            if len(word) != len(pattern):
                continue
            d_pw = {}
            d_wp = {}
            has_pattern = True
            for w, p in zip(word, pattern):
                if p not in d_pw:
                    if w in d_wp and d_wp[w] != p:
                        has_pattern = False
                        break
                    d_pw[p] = w
                    d_wp[w] = p
                elif d_pw[p] != w:
                    has_pattern = False
                    break
            if has_pattern:
                ret.append(word)
        return ret