class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        cost = [ [0] * n for _ in range(0, m)]
        #cost = grid # to speed up, though destroy grid
        cost[0][0] = grid[0][0]

        
        for j in range(1, n): # row 0 accumulate sum
            cost[0][j] = grid[0][j] + cost[0][j-1]
        for i in range(1, m): # column 0 accumulate sum
            cost[i][0] = grid[i][0] + cost[i-1][0]
        
        
        for i in range(1, m):
            for j in range(1, n):
                if cost[i-1][j] < cost[i][j-1]:
                    cost[i][j] = grid[i][j] + cost[i-1][j]
                else:
                    cost[i][j] = grid[i][j] + cost[i][j-1]
                #cost[i][j] = grid[i][j] + min(cost[i-1][j], cost[i][j-1])
        
        return cost[-1][-1]