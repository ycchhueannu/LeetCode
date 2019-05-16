class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        d = {}
        for card in deck:
            if card not in d:
                d[card] = 1
            else:
                d[card] += 1
        
        num = list(d.values())
        min_n = min(num)
        
        for num_split in range(2, min_n+1):
            can_split = all(i % num_split == 0 for i in num)
            if can_split:
                return True
        return False