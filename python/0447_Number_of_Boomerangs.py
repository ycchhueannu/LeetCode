class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for i in range(0, len(points)):
            di = {}
            for j in range(0, len(points)):
                dist = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                
                if dist not in di:
                    di[dist] = 1
                else:
                    cnt += di[dist]
                    di[dist] += 1

        return 2*cnt
"""
** NOTE THAT WE DON'T NEED STORE pi in d[dist][pi] since we don't need it anymore (we 
only care about the final answer), I move d into the first for loop, rename it as di,
and drop the conversion from list to tuple **
** NOTE ALSO THAT I REARRANGE how to count the final answer (variable "cnt") to 
make it faster **

# version 4 is accepted but slow, we can see that cnt is computed in the nested for
# loop since we know that if current number n is d[dist][pi], then the number of 
# increase is n*(n-1) - (n-1)*(n-2) = 2*(n-1)
        d = {}
        cnt = 0
        for i in range(0, len(points)):
            for j in range(0, len(points)):
                if j == i:
                    continue
                dist = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                
                pi = tuple(points[i])
                    
                if dist not in d:
                    d[dist] = {}
                if pi not in d[dist]:
                    d[dist][pi] = 1
                else:
                    d[dist][pi] += 1
                    cnt += 2*(d[dist][pi]-1)

        return cnt
"""

"""
BELOWS ARE TLE SOLUTION:

# version 1 will TLE, this solution is straightforward O(N^3)
        cnt = 0
        for i in range(0, len(points)):
            for j in range(0, len(points)):
                if j == i:
                    continue
                d1 = (points[i][0] - points[j][0])**2 + (points[i][1]-points[j][1])**2
                for k in range(0, len(points)):
                    if k == j or k == i:
                        continue
                    d2 = (points[i][0] - points[k][0])**2 + (points[i][1]-points[k][1])**2
                    if d1 == d2:
                        cnt += 1
                
        return cnt

# version 2 will also TLE, but this introduce hash table (use tuple as key) and then
# introduce the permutation formula to count the final solution, e.g. P(n,2) = n(n-1) 
        d = {}
        for i in range(0, len(points)):
            for j in range(0, len(points)):
                if j == i:
                    continue
                dist = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                
                pi = tuple(points[i])
                pj = tuple(points[j])
                    
                if dist not in d:
                    d[dist] = {}
                if pi not in d[dist]:
                    d[dist][pi] = {pj}
                else:
                    d[dist][pi].add(pj)
        
        cnt = 0
        for dist in d:
            for pivot in d[dist]:
                cnt += (len(d[dist][pivot])-1)*(len(d[dist][pivot]))
        return cnt

# version 3 is basically the same as version 2, except we don't care which points
# make a bommerang, so pj is useless (TLE also)
        d = {}
        for i in range(0, len(points)):
            for j in range(0, len(points)):
                if j == i:
                    continue
                dist = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                
                pi = tuple(points[i])
                #pj = tuple(points[j])
                    
                if dist not in d:
                    d[dist] = {}
                if pi not in d[dist]:
                    d[dist][pi] = 1
                    #d[dist][pi] = {pj}
                else:
                    d[dist][pi] += 1
                    #d[dist][pi].add(pj)
        
        cnt = 0
        for dist in d:
            for pivot in d[dist]:
                cnt += (d[dist][pivot]-1)*(d[dist][pivot])

        return cnt
"""