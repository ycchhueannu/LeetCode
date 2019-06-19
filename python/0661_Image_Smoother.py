class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(0, len(M)):
            ret.append([])
            for j in range(0, len(M[0])):
                surrounding_sum = M[i][j]
                cnt = 1
                for di, dj in directions:
                    new_i, new_j = i+di, j+dj
                    if (0 <= new_i < len(M)) and (0 <= new_j < len(M[0])):
                        surrounding_sum += M[new_i][new_j]
                        cnt += 1
                ret[i].append(surrounding_sum // cnt)
        
        return ret