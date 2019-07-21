class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            if len(w) not in d:
                d[len(w)] = {w}
            else:
                d[len(w)].add(w)
        
        not_visit = set(words)
        ret = 0
        
        def DFS(w, cur_chain_len):
            next_visit_len = len(w) + 1
            if next_visit_len not in d:
                return cur_chain_len
            max_chain_len = cur_chain_len
            for next_w in d[next_visit_len]:
                if (next_w in not_visit) and set(w).issubset(set(next_w)):
                    not_visit.remove(next_w)
                    max_chain_len = max(max_chain_len, DFS(next_w, cur_chain_len+1))
            return max_chain_len
        
        for l in sorted(d.keys()):
            for w in d[l]:
                if w in not_visit:
                    not_visit.remove(w)
                    ret = max(ret, DFS(w, 1))
        
        return ret