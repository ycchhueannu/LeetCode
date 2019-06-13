class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        cur_sum = 0
        ret = []
        for a in A:
            if a % 2 == 0:
                cur_sum += a
        for val, index in queries:
            pre_Ai = A[index]
            A[index] += val
            if A[index] % 2 == 0:
                if pre_Ai % 2:
                    cur_sum += A[index]
                else:
                    cur_sum += val
            elif pre_Ai % 2 == 0 and A[index] % 2:
                cur_sum -= pre_Ai
            ret.append(cur_sum)
        
        return ret