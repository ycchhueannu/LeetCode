class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # key: perimeter (e.g. 3 is the block that only connects 1)
        # normally key=4 is not happening, unless grid = [[1]]
        d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        i_min, i_max = 0, len(grid)-1
        j_min, j_max = 0, len(grid[0])-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                if i in [i_min, i_max] or j in [j_min, j_max]:
                    if i == i_min: left = 0
                    else: left = grid[i-1][j]
                        
                    if i == i_max: right = 0
                    else: right = grid[i+1][j]
                    
                    if j == j_min: up = 0
                    else: up = grid[i][j-1]
                    
                    if j == j_max: down = 0
                    else: down = grid[i][j+1]
                    
                    cnt = abs(left+right+up+down-4)
                    d[cnt] += 1
                        
                else:
                    cnt = abs(grid[i-1][j]
                             + grid[i+1][j] 
                             + grid[i][j-1]
                             + grid[i][j+1] 
                             - 4)
                    d[cnt] += 1
        
        return d[1]*1 + d[2]*2 + d[3]*3 + d[4]*4