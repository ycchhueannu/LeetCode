class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        from itertools import combinations
        ret = 0
        for i, j, k in combinations(points, 3):
            ret = max(ret, 0.5*abs((j[0]-i[0])*(k[1]-i[1]) - (j[1]-i[1])*(k[0]-i[0])))
        return ret