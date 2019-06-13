class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ret = 0
        for i, j in zip(heights, sorted(heights)):
            if i != j:
                ret += 1
        return ret