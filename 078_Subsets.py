from itertools import combinations, chain
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list( chain.from_iterable (map( lambda x: map(list, combinations(nums, x)), range(0, len(nums)+1) ) ) ) 
