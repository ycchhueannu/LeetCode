class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        matrix[:] = zip(*matrix[::-1]) # note that zip return list of tuples however in LeetCode it seems that it treat it as list?