class Solution(object):
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def convert_square(board):
            board_sqr = [[[] for _ in range(3)] for _ in range(3)]
            for idx, row in enumerate(board):
                if idx <= 2:
                    i = 0
                elif idx <= 5:
                    i = 1
                else:
                    i = 2
                board_sqr[i][0].extend(row[:3])
                board_sqr[i][1].extend(row[3:6])
                board_sqr[i][2].extend(row[6:])
            return [numbers for rows in board_sqr for numbers in rows] # flatten
    
        def notValid(numbers):
            from collections import Counter
            counter = Counter(numbers)
            if all(counter.get(str(i)) in [None, 1] for i in range(1, 10)):
                return False
            else:
                return True
            
        for row in board:
            if notValid(row):
                return False
            
        board_t = list(map(list, zip(*board))) # transpose of board
        for col in board_t:
            if notValid(col):
                return False
        
        board_sqr = convert_square(board) # 3x3 square
        for sqr in board_sqr:
            if notValid(sqr):
                return False
        
        return True