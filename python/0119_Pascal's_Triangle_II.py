class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        
        prev_row = [1,1]
        for i in range(2, rowIndex+2):
            cur_row = [1]
            for j in range(1, i-1):
                cur_row.append(prev_row[j-1] + prev_row[j])
            cur_row.append(1)
            prev_row = cur_row
        return cur_row