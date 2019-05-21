class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), len(candies)//2)
        """
        # NOTE THAT the last if-statement can be re-written
        # since "dup_kind >= sis_get - uni_kind" is equal to
        # "num_kind >= sis_get", and "uni_kind + dup_kind"
        # equals num_kind
        d = {}
        for c in candies:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        num_kind = len(d)
        dup_kind = 0
        for i in d:
            if d[i] > 1:
                dup_kind += 1
        uni_kind = num_kind - dup_kind
        
        sis_get = len(candies) // 2
        
        if uni_kind >= sis_get:
            return sis_get
        elif dup_kind >= sis_get - uni_kind:
            return sis_get
        else:
            return uni_kind + dup_kind
        """