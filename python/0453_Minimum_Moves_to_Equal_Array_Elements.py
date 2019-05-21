class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # W.L.O.G., let a1 <= a2 <= ... <= an
        # sum(nums) + (n-1)*step = n * new_ave
        # new_ave =  a1 + step. Thus, step =
        # sum(nums) - n*a1
        return sum(nums) - len(nums)*min(nums)
        
        """
        # ver 2, ideas are as follows:
        # note that prime denote the smallest
        # Round 1: nums = [1, 7, 16, 19], +18
        # Round 2: nums = [19', 25, 34, 19]
        #              -> [19', 19, 25, 34], +15
        # Round 3: nums = [34', 34, 40, 34]
                       -> [34', 34, 34, 40], +6
        # Round 4: nums = [40', 40, 40, 40]
        # no matters the how the process goes,
        # minimum number, i.e. a1, will always be
        # added (see num w/ prime)
        # we can verify that 18+15+6 = 39 = 40-1
        
        # ver 1 will TLE, can be reduced
        from collections import deque
        dq = deque(nums)
        cnt = 0
        while dq[0] != dq[-1]:
            add = dq[-1] - dq[0]
            cnt += add
            for i in range(0, len(dq)-1):
                dq[i] += add
            dq.appendleft(dq.pop())
        return cnt
        """