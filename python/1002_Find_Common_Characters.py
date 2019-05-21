class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if len(A) == 1:
            return list(A[0])
        alphabet = map(chr, range(97, 123))
        d = {i: 0 for i in alphabet}
        for w in A[0]:
            d[w] += 1
            
        for i in range(1, len(A)):
            tmp_d = {i: 0 for i in alphabet}
            for w in A[i]:
                tmp_d[w] += 1
            
            d = {i: min(d[i], tmp_d[i]) for i in alphabet}
                
        return [i for i in d for j in range(0, d[i])]