class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m + n == 2: # m == 1 and n == 1
            return 1 # obstacleGrid[0][0] = 1 is handled above
        
        else:
            #path = [[0] * (n+1)] * (m+1) # will not work, since each row's reference is point to the same object
            path = list(map(lambda x: [1]+[0]*n, range(0, m+1))) # note that row 0 is not needed

        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1]:
                    path[i][j] = 0
                    continue
                    
                if 1 in (i, j):
                    path[i][j] = path[i][j-1] if i == 1 else path[i-1][j]

                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]

        #for p in path:
        #    print(p)
        return path[-1][-1]