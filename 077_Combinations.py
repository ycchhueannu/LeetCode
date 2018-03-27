from itertools import combinations
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(map(list, combinations(range(1, n+1), k)))