class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        
        pascal_row = [[1], [1,1]]
        for i in range(3, numRows+1):
            cur_row = [1]
            for j in range(1, i-1):
                cur_row.append(pascal_row[i-2][j-1] + pascal_row[i-2][j])
            cur_row.append(1)
            pascal_row.append(cur_row)
        return pascal_row