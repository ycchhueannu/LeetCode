class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        max_i = len(matrix)
        max_j = len(matrix[0])
        for i in range(0, max_i):
            cur_element = matrix[i][0]
            next_i, next_j = i+1, 1
            while next_i < max_i and next_j < max_j:
                if matrix[next_i][next_j] == cur_element:
                    next_i += 1
                    next_j += 1
                else:
                    return False
        for j in range(0, max_j):
            cur_element = matrix[0][j]
            next_i, next_j = 1, j+1
            while next_i < max_i and next_j < max_j:
                if matrix[next_i][next_j] == cur_element:
                    next_i += 1
                    next_j += 1
                else:
                    return False
        return True