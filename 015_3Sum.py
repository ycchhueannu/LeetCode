from collections import Counter
from itertools import combinations
from itertools import chain

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) < 3:
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        nums.sort() # a little bit faster..?
        d = Counter(nums) # Counter return dictionary
        
        #new_nums = [ val for _ in range(d[val]) for val in d] # wrong
        new_nums = list( chain.from_iterable([[val]*min(d[val],3) for val in d]) ) # optimize?
        
        #print(new_nums)
        
        val_comb = combinations(new_nums, 2) # value combinations
        #idx_comb = combinations(range(0, len(new_nums)), 2) # index combinations
        
        
        s = set()
        for val_tup in val_comb:
            need = -sum(val_tup)
            if ( need in d ) and ( (d[need] - val_tup.count(need)) > 0 ):
                s.add( tuple (sorted([val_tup[0], val_tup[1], need]) ) )
                #s.add( frozenset([val_tup[0], val_tup[1], need]) ) # frozenset not implement here = =
        
        return list(s)