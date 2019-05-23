class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {v: i  for i,v in enumerate(order)}

        for i in range(0, len(words)-1):
            min_len = min(len(words[i]), len(words[i+1]))
            lt = False
            for j in range(min_len):
                #print(d[words[i][j]], d[words[i+1][j]])
                if d[words[i][j]] > d[words[i+1][j]]:
                    return False
                elif d[words[i][j]] < d[words[i+1][j]]:
                    lt = True
                    break
            if not lt and len(words[i]) > len(words[i+1]):
                return False
        return True