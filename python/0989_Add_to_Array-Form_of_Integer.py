class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        K_list = []
        while K > 0:
            K_list.append(K%10)
            K //= 10
            
        cr = 0
        k = 0
        for i in range(len(A)-1, -1, -1):
            if k < len(K_list):
                A[i] += cr + K_list[k]
                k += 1
                if A[i] >= 10:
                    cr = 1
                    A[i] %= 10
                else:
                    cr = 0
            else:
                A[i] += cr
                if A[i] >= 10:
                    cr = 1
                    A[i] %= 10
                else:
                    cr = 0
        
        while k < len(K_list):
            A = [cr + K_list[k]] + A
            k += 1
            if A[0] >= 10:
                cr = 1
                A[0] %= 10
            else:
                cr = 0
        
        if cr == 1:
            A = [1] + A
        return A