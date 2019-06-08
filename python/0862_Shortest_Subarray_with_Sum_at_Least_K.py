class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 1:
            if A[0] >= K:
                return 1
            return -1
        
        from collections import deque
        q = deque([0]) # cumulative sum
        min_len = float("inf")
        for a in A:
            q.append(q[-1]+a)
        #print(q)
        tmp_q = deque()
        ret = float("inf")
        for i, v in enumerate(q):
            while len(tmp_q) and v - tmp_q[0][1] >= K:
                ret = min(ret, i-tmp_q[0][0])
                tmp_q.popleft()
            while len(tmp_q) and v <= tmp_q[-1][1]:
                tmp_q.pop()
            tmp_q.append([i, v])
        
        if ret == float("inf"):
            return -1
        else:
            return ret

# A = [-2, -1, -2], K = -1 # no such case since K >= 1
# A = [-3, 4, -2, 1, 2, 3], K = 5
# A = [-3, 4, -2, 1, -2, 2, 3], K = 5
# A = [1, 2, 5, -1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1], K = 7
# A = [1, 2, 5, -1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], K = 7
# A = [1, 2, 1, -2, 10, 1, 1, -10, 9, 1, 1, 1, 1, 1, 1], K = 13