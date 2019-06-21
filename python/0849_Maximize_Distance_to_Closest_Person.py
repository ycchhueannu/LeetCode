class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        pre_oi = -1 # one index
        pre_zi = 0 # zero index
        init = False
        ret = 1
        for i in range(len(seats)):
            if seats[i] == 0:
                if not init:
                    init = True
                    pre_zi = i
            else:
                init = False
                if pre_oi < 0:
                    ret = max(ret, i-pre_zi)
                    pre_oi = i
                else:
                    if pre_oi < pre_zi:
                        ret = max(ret, (i-1-pre_zi)//2 + 1)
                    pre_oi = i
        if init:
            ret = max(ret, i-pre_zi+1)
        return ret
"""
Note that line 23 consider both odd and even in 0 subsequence:
if odd, then the computed distance should be ((i-1)-zi)//2 + 1,
which is (i-1-zi)//2 + 1.
[1,  0,  0,  0,  0,  0,  1]
    zi              i-1  i

if even, then the computed distance should be ((i-1)-zi+1)//2,
which is (i-zi)//2, we can rewrite it as (i-1-zi)//2 + 1.
[1,  0,  0,  0,  0,  0,  0,  1]
    zi                  i-1  i

Note also that pre_oi is to let me know if the LHS of zero 
subsequence has one
"""