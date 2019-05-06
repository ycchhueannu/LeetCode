class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        ret = []
        for query in queries:
            i, j = 0, 0
            while i < len(query) and j < len(pattern):
                if query[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    if query[i].isupper():
                        ret.append(False)
                        break
                    else:
                        i += 1
                if i == len(query):
                    if pattern[j:]:
                        ret.append(False)
                    else:
                        ret.append(True)
                    continue
                    
                if j == len(pattern):
                    if any(q.isupper() for q in query[i:]):
                        ret.append(False)
                    else:
                        ret.append(True)
                    
            
        return ret