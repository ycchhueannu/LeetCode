class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dA = []
        for i in range(1, len(A)):
            dA.append(A[i]-A[i-1])
        pre_d = None
        cnt = 0
        ret = 0
        for i in dA:
            if pre_d is None:
                pre_d = i
                cnt = 1
            elif i != pre_d:
                ret += cnt*(cnt-1)/2
                pre_d = i
                cnt = 1
            else:
                cnt += 1
        if cnt != 0:
            ret += cnt*(cnt-1)/2
        return ret